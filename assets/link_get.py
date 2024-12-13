import requests
import logging
import random
import os

# Настройка логгирования
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("GoogleVideoUtils")

class GoogleVideoUtils:
    # Маппинг символов из Java-кода
    letters_list_a = list('uzpkfa50vqlgb61wrmhc72xsnid83ytjo94-')
    letters_list_b = list('0123456789abcdefghijklmno-pqrstuvwxyz-')
    letters_map = dict(zip(letters_list_a, letters_list_b))

    @staticmethod
    def generate_google_video_domains(count=19):
        domains = []

        # Удаляем файл, если он уже существует
        if os.path.exists("links.txt"):
            os.remove("links.txt")

        for _ in range(count):
            cluster_codename = GoogleVideoUtils.generate_random_codename()
            cluster_name = GoogleVideoUtils.convert_cluster_codename(cluster_codename)
            auto_gcs = GoogleVideoUtils.build_auto_gcs(cluster_name)
            logger.info(f"Сгенерированный домен: {auto_gcs}")
            domains.append(auto_gcs)

        # Дополнительные статичные домены без изменений
        extra_domains = [
            "www.youtube.com",
            "yt3.ggpht.com",
            "yt4.ggpht.com",
            "i.ytimg.com",
            "manifest.googlevideo.com",
            "signaler-pa.googlevideo.com",
        ]
        domains.extend(extra_domains)

        # Удаляем дубликаты доменов
        unique_domains = list(set(domains))

        # Записываем в файл
        with open("links.txt", "w") as file:
            for domain in unique_domains:
                file.write(f"{domain}\n")
        logger.info(f"Доменов записано в links.txt: {len(unique_domains)}")

    @staticmethod
    def generate_random_codename(length=10):
        # Генерация случайного кодового имени из letters_list_a
        while True:
            codename = ''.join(random.choices(GoogleVideoUtils.letters_list_a, k=length))
            if codename[-1] != '-':  # Проверка, чтобы последний символ не был дефисом
                return codename

    @staticmethod
    def convert_cluster_codename(cluster_codename: str) -> str:
        cluster_name_builder = []
        for char in cluster_codename:
            mapped_char = GoogleVideoUtils.letters_map.get(char)
            if mapped_char:
                cluster_name_builder.append(mapped_char)
            else:
                logger.warning(f"Символ '{char}' не найден в маппинге")
        return ''.join(cluster_name_builder)

    @staticmethod
    def build_auto_gcs(cluster_name: str) -> str:
        return f"rr1---sn-{cluster_name}.googlevideo.com"
if __name__ == "__main__":
    GoogleVideoUtils.generate_google_video_domains(count=19)
