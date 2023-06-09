# IO

Here is an overview of the filters defined in the IO family.

### Content

Opens the input as a file, and returns its content in a bytearray. The default mode is binary, but an optional "mode" parameter can be specified to get text data (with the value "r" instead of the default "rb").

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