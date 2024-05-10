import requests

def main():
    url = input("Enter the URL to check: ")
    api_key = input("Enter your VirusTotal API key: ")
    
    result = check_url(url, api_key)
    if result['response_code'] == 1:
        print("URL:", url)
        print("Scan date:", result['scan_date'])
        print("Total scans:", result['total'])
        print("Positives:", result['positives'])
        print("Scan results:")
        for scanner, result in result['scans'].items():
            print("\t{}: {}".format(scanner, result['result']))
    else:
        print("No results found for this URL.")

urls = []
scan_results = []

try:
    with open(filename, 'r') as f:
      for line in f:
        url = line.strip()  # Remove leading/trailing whitespace
        urls.append(url)

    #vt_url = "https://www.virustotal.com/v2/urls"

    for url in urls:
      headers = {"Authorization": f"Bearer {api_key}"}
      params = {"url": url}

      response = requests.get(vt_url, headers=headers, params=params)

      if response.status_code == 200:
        scan_data = response.json()
        scan_results.append({"url": url, "scan_data": scan_data})
      else:
        print(f"Error getting report for {url}: {response.status_code}")

  except Exception as e:
    print(f"An error occurred: {e}")
    raise

  return scan_results


if __name__ == "__main__":
    main()



