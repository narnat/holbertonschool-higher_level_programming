#!/usr/bin/python3
"""
   Heap modifier
   Usage: read_write_heap.py pid search_string replace_string
   Src:
     https://blog.holbertonschool.com/hack-the-virtual-memory-c-strings-proc/
   Removed some comments
"""
import sys


def error():
    print('Usage: read_write_heap.py pid search_string replace_string')
    sys.exit(1)

if len(sys.argv) != 4 or int(sys.argv[1]) <= 0:
    error()
pid = int(sys.argv[1])

search_string, write_string = sys.argv[2:]

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

    try:
        addr, perm, offset, device, inode = sline[:5]
        pathname = sline[-1][:-1]
    except:
        print("Error")
        maps_file.close()
        sys.exit(1)

    if perm[0] != 'r' or perm[1] != 'w':
        print("{} does not have read/write permission".format(pathname))
        maps_file.close()
        sys.exit(1)

    addr = addr.split("-")
    if len(addr) != 2:
        print("Wrong addrress format")
        maps_file.close()
        sys.exit(1)

    addr_start, addr_end = int(addr[0], 16), int(addr[1], 16)

    try:
        mem_file = open(mem, 'rb+')
    except:
        print("ERROR")
        maps_file.close()
        sys.exit(1)

    try:
        mem_file.seek(addr_start)
        heap = mem_file.read(addr_end - addr_start)
    except:
        print("ERROR")
        maps_file.close()
        mem_file.close()
        sys.exit(1)

    try:
        i = heap.index(bytes(search_string, "ASCII"))
    except Exception:
        print("Can't find '{}'".format(search_string))
        maps_file.close()
        mem_file.close()
        sys.exit(1)

    try:
        mem_file.seek(addr_start + i)
        mem_file.write(bytes(write_string+'\0', "ASCII"))
        print("***Done***")
    except:
        print("Error")
        maps_file.close()
        sys.exit(1)

    try:
        maps_file.close()
        mem_file.close()
    except:
        print("Error")
        maps_file.close()
        sys.exit(1)
    break
