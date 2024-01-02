# cloudflareDynamicDNS

## Introduction
cloudflareDynamicDNS is a project designed to automatically update your public IP on Cloudflare at specified intervals. This functionality is particularly useful for accessing your server via a domain, ensuring that the domain always points to the current public IP of your server.

## Usage

To use this tool, follow these steps:

1. Rename the `config.example.json` file to `config.json`.
2. Fill in the necessary details in the `config.json` file.

Once you have configured your settings, you can run the script with the following command:

```bash
python3 main.py
```

## License

MIT License