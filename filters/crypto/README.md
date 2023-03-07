# Crypto

Here is an overview of the filters defined in the Crypto family.

### XOR

Generates a random single-byte XOR key, receives an input and returns itself XORed byte-wise with the single-byte key. The variable `XOR_KEY` will be replaced by the generated key.

```jinja
namespace Hackcraft
{
    class Malware
    {
        public static int KEY = {{ XOR_KEY }};

        public static readonly byte[] payload = {{ "malicious.dll" | content | xor | hexarr }};
    }
}

```

### AES

Generates a random AES key and IV, receives an input and returns the AES-CBC cipher-text of the input. The variable `AES_KEY` and `AES_IV` will be replaced by the generated key and IV, respectively.

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