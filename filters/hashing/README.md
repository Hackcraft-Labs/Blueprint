# Hashing

Here is an overview of the filters defined in the Hashing family.

### DJB2

Returns the DJB2 hash of the input, using the seed 0x7734773477347734. 

```jinja
// populate api hashes in table.
table->NtAllocateVirtualMemory.dwHash = {{ "NtAllocateVirtualMemory" | djb2 }};
```