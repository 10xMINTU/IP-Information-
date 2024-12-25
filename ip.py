import requests

def get_ip_info(ip=""):
    # Base API URL
    url = f"http://ipinfo.io/{ip}/json"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return {
                "IP": data.get("ip", "N/A"),
                "City": data.get("city", "N/A"),
                "Region": data.get("region", "N/A"),
                "Country": data.get("country", "N/A"),
                "Location": data.get("loc", "N/A"),
                "ISP": data.get("org", "N/A"),
            }
        else:
            return {"error": f"Failed to retrieve information. Status code: {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    print("IP Address Information Gathering Tool")
    print("-" * 40)
    
    user_ip = input("Enter an IP address (or leave blank for your IP): ").strip()
    ip_info = get_ip_info(user_ip)
    
    print("\nIP Address Information:")
    for key, value in ip_info.items():
        print(f"{key}: {value}")
