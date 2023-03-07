# Format

Here is an overview of the filters defined in the Format family.

### HexArray

Returns the input converted to a string containing each byte in hex, seperated by commas. 

```jinja
namespace Hackcraft
{
    class Malware
    {
        public static readonly byte[] aesKey = new byte[] { {{ AES_KEY | hexarr }} };
        public static readonly byte[] aesIv = new byte[] { {{ AES_IV | hexarr }} };

        public static readonly byte[] payload = new byte[] { {{ "payload.bin" | content | aes | hexarr }} };
    }
}
```

### DecArray

Returns the input converted to a string containing each byte in decimal, seperated by commas. It is usefull for languages that do not natively suppport the `0x` prefix for hex literals.

```jinja
namespace Hackcraft
{
    class Malware
    {
        public static readonly byte[] aesKey = new byte[] { {{ AES_KEY | decarr }} };
        public static readonly byte[] aesIv = new byte[] { {{ AES_IV | decarr }} };

        public static readonly byte[] payload = new byte[] { {{ "payload.bin" | content | aes | decarr }} };
    }
}
```