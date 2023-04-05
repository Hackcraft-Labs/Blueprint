# Blueprint

A modular source code templater.

# Configuration

Blueprint expects to receive a JSON configuration file which looks like the following:
```json
{
    "filters": [
        "crypto.AES",
        "fmt.HexArray",
        "io.Content"
    ],
    "targets": [
        {
            "input": "Example.h.tpl",
            "output": "Example.h",
            "variables": {
                "EXAMPLE_VARIABLE": "EXAMPLE_VALUE",
            }
        }
    ]
}
```

The configuration is comprised of an arbitrary number of file `targets`. Blueprint operates on those targets by reading the input file of each target, performing templating on it, and writing the result to the output file, replacing any variables (found in the `variables` section) with their values. Moreover, an array of `filters` is defined in the config, controlling which filters will be imported (and thus be available for usage) in this configuration.

# Templating

Blueprint utilizes [Jinja](https://jinja.palletsprojects.com/en/3.1.x/) for templating. Building upon the configuration in the above example, here is Example.h.tpl:
```jinja
unsigned char key[] = { {{ AES_KEY | hexarr }} };
unsigned char iv[] = { {{ AES_IV | hexarr }} };
unsigned char payload[] = { {{ "payload.bin" | content | aes | hexarr }} };
usigned char example = "{{ EXAMPLE_VARIABLE }}";
```

Everything defined in `{{ }}` blocks is going to be evaluated by Blueprint. Inside such blocks, Jinja syntax is valid, along with filters defined by Blueprint modules. Filters receive an input (the expression before the pipe `|`) and return an output. They can also be chained together to create intricate templating functionality. Many filters also apply their own replacements to the processed target file, e.g. the XOR filter which also replaces `XOR_KEY` in the file with the random key generated for XORing.

# Filters
For documentation regarding each filter refer to the README file inside the filter's directory. Here is a list of the available filters:
- [io.Content](https://github.com/Hackcraft-Labs/Blueprint/blob/main/filters/io)
- [io.Output](https://github.com/Hackcraft-Labs/Blueprint/blob/main/filters/io)
- [crypto.XOR](https://github.com/Hackcraft-Labs/Blueprint/blob/main/filters/crypto)
- [crypto.AES](https://github.com/Hackcraft-Labs/Blueprint/blob/main/filters/crypto)
- [fmt.HexArray](https://github.com/Hackcraft-Labs/Blueprint/blob/main/filters/fmt)
- [fmt.DecArray](https://github.com/Hackcraft-Labs/Blueprint/blob/main/filters/fmt)
- [hashing.DJB2](https://github.com/Hackcraft-Labs/Blueprint/blob/main/filters/hashing)
  
# Custom Modules
For documentation regarding creating your own Blueprint filters, refer to this [README](https://github.com/Hackcraft-Labs/Blueprint/blob/main/filters).

### Community

Join the Hackcraft community discord server [here](https://discord.gg/KZZfsnQsja). On the server you can receive support and discuss issues related to Blueprint.