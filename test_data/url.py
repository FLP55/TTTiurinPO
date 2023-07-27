class MainURL:
    @staticmethod
    def get_url_from_dict(key: str) -> str:
        all_url = {"base_url": "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?"}
        return all_url[key]