import json

class Config:
    def __init__(self, file: str) -> None:
        self.file = file
        self.req_keys = ["token", "guilds"]
        self.cfg = {"prefix":".", "status":"online"}

        try:
            f = open(self.file)
            config = json.loads(f.read())
            f.close()

            for key in config.keys():
                self.cfg[key] = config[key]

            for key in self.req_keys:
                if not key in self.cfg.keys():
                    raise Exception(f"'{key}' is required and not found in config")

        except FileNotFoundError:
            raise Exception(f"Create the config file: '{file}'")

        except  json.decoder.JSONDecodeError:
            raise Exception(f"'{file}' is not in JSON format")    