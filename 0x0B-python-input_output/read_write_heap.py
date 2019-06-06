#!/usr/bin/python3
"""
   Heap modifier
   Usage: read_write_heap.py pid search_string replace_string
   Src: https://blog.holbertonschool.com/hack-the-virtual-memory-c-strings-proc/
   Removed some comments
"""
import sys


def error():
    print('Usage: read_write_heap.py pid search_string replace_string')
    sys.exit(1)

if len(sys.argv) != 4 or int(sys.argv[1]) <= 0:
    error()
pid = int(sys.argv[1])

search_string = str(sys.argv[2])
write_string = str(sys.argv[3])
maps = "/proc/{}/maps".format(pid)
mem = "/proc/{}/mem".format(pid)

try:
    maps_file = open(maps, 'r')
except:
    print("ERROR")
    sys.exit(1)

for line in maps_file:
    sline = line.split(' ')
    if sline[-1][:-1] != "[heap]":
        continue

    addr = sline[0]
    perm = sline[1]
    offset = sline[2]
    device = sline[3]
    inode = sline[4]
    pathname = sline[-1][:-1]
    print("\tpathname = {}".format(pathname))
    print("\taddresses = {}".format(addr))
    print("\tpermisions = {}".format(perm))
    print("\toffset = {}".format(offset))
    print("\tinode = {}".format(inode))

    if perm[0] != 'r' or perm[1] != 'w':
        print("{} does not have read/write permission".format(pathname))
        maps_file.close()
        exit(0)


    addr = addr.split("-")
    if len(addr) != 2:
        print("[*] Wrong addr format")
        maps_file.close()
        exit(1)
    addr_start = int(addr[0], 16)
    addr_end = int(addr[1], 16)
    print("\tAddr start [{:x}] | end [{:x}]".format(addr_start, addr_end))

    try:
        mem_file = open(mem, 'rb+')
    except IOError as e:
        print("[ERROR] Can not open file {}:".format(mem))
        print("        I/O error({}): {}".format(e.errno, e.strerror))
        maps_file.close()
        exit(1)

    mem_file.seek(addr_start)
    heap = mem_file.read(addr_end - addr_start)

    try:
        i = heap.index(bytes(search_string, "ASCII"))
    except Exception:
        print("Can't find '{}'".format(search_string))
        maps_file.close()
        mem_file.close()
        exit(0)
    print("[*] Found '{}' at {:x}".format(search_string, i))

    print("[*] Writing '{}' at {:x}".format(write_string, addr_start + i))
    mem_file.seek(addr_start + i)
    mem_file.write(bytes(write_string, "ASCII"))

    maps_file.close()
    mem_file.close()
    break
