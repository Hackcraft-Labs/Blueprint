# IO

Here is an overview of the filters defined in the IO family.

### Content

Opens the input as a file, and returns its binary content in a bytearray.

```jinja
namespace Hackcraft
{
    class Malware
    {
        public static readonly byte[] payload = new byte[] { {{ "payload.bin" | content | hexarr }} };
    }
}
```

### Output

Opens the file provied in the `name` parameter, and writes the input to it.

```jinja
{{ "example.dll" | content | xor | output(name="xored.bin") }}
```