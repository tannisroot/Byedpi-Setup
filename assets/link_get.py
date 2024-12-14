import re
import requests

def generate_google_video_domain():
    def get_cluster_codename():
        urls = [
            "https://redirector.gvt1.com/report_mapping?di=no",
            "https://redirector.googlevideo.com/report_mapping?di=no"
        ]
        
        letters_list_a = [
            'u', 'z', 'p', 'k', 'f', 'a', '5', '0', 'v', 'q', 'l', 'g',
            'b', '6', '1', 'w', 'r', 'm', 'h', 'c', '7', '2', 'x', 's',
            'n', 'i', 'd', '8', '3', 'y', 't', 'o', 'j', 'e', '9', '4', '-'
        ]
        letters_list_b = [
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b',
            'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '-'
        ]
        letters_map = dict(zip(letters_list_a, letters_list_b))
        
        for url in urls:
            try:
                response = requests.get(url, timeout=2)
                if response.status_code == 200:
                    match = re.search(r"=>\s*(\S+)\s*(?:\(|:)", response.text)
                    if match:
                        cluster_codename = match.group(1).rstrip('.: ')
                        
                        # Преобразование кодового названия
                        converted_name = ''.join(
                            letters_map.get(char, '') for char in cluster_codename
                        )
                        
                        # Формирование домена
                        domain = f"rr1---sn-{converted_name}.googlevideo.com"
                        return domain
            except Exception as e:
                print(f"Ошибка получения домена: {e}")
        
        return None

    # Предопределенный список доменов
    predefined_domains = [
        "www.youtube.com",
        "manifest.googlevideo.com",
        "i.ytimg.com",
        "yt3.ggpht.com",
        "yt4.ggpht.com",
        "signaler-pa.youtube.com",
        "jnn-pa.googleapis.com",
        "rr1---sn-4axm-n8vs.googlevideo.com",
        "rr1---sn-gvnuxaxjvh-o8ge.googlevideo.com",
        "rr1---sn-ug5onuxaxjvh-p3ul.googlevideo.com", 
        "rr1---sn-ug5onuxaxjvh-n8v6.googlevideo.com",
        "rr4---sn-q4flrnsl.googlevideo.com",
        "rr10---sn-gvnuxaxjvh-304z.googlevideo.com",
        "rr1---sn-8ph2xajvh-5xge.googlevideo.com",
        "rr1---sn-gvnuxaxjvh-5gie.googlevideo.com",
        "rr12---sn-gvnuxaxjvh-bvwz.googlevideo.com",
        "rr1---sn-u5uuxaxjvhg0-ocje.googlevideo.com",
        "rr2---sn-q4fl6ndl.googlevideo.com", 
        "rr5---sn-gvnuxaxjvh-n8vk.googlevideo.com",
        "rr4---sn-jvhnu5g-c35d.googlevideo.com",
        "rr1---sn-q4fl6n6y.googlevideo.com",
        "rr2---sn-hgn7ynek.googlevideo.com"
    ]

    # Получаем новый домен
    new_domain = get_cluster_codename()
    
    # Если новый домен получен, добавляем его к списку
    if new_domain and new_domain not in predefined_domains:
        predefined_domains.append(new_domain)
    
    # Сохраняем все домены в файл
    with open('links.txt', 'w') as f:
        for domain in predefined_domains:
            f.write(domain + '\n')
    
#    print(f"Сохранено доменов: {len(predefined_domains)}")
#    print("Новый домен:", new_domain if new_domain else "Не удалось получить")

# Запуск
generate_google_video_domain()
