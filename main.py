import datetime
import os
import random
import pythonping
import time

# CONSTANTS VALUE
OUTPUT_PATH = "outputs/results.csv"
"""
TEST_SERVER_URL: string | string[]

- Option 1:
    TEST_SERVER_URL = "1.1.1.1"
- Option 2:
    TEST_SERVER_URL = ["1.1.1.1", "www.google.com"]
"""
TEST_SERVER_URL = ["1.1.1.1", "www.google.com"]
PING_INTERVAL_IN_SEC = 1
# END CONSTANTS VALUE


def init_logger():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    file_open_mode = "a+"
    if os.path.exists(OUTPUT_PATH):
        file_open_mode = "r+"

    with open(OUTPUT_PATH, file_open_mode) as f:
        f.seek(0)
        f.write("timestamp,server,res_time_ms\n")
    os.chmod(OUTPUT_PATH, 0o666)


def ping_server(server_url: str):
    response = pythonping.ping(server_url, timeout=3, count=1)
    if response .packets_lost > 1:
        return None
    return response.rtt_avg_ms


def log_response(ping_in_ms, server_url: str):
    current_datetime = datetime.datetime.now()
    current_timestamp = int(current_datetime.timestamp())

    with open(OUTPUT_PATH, 'a') as f:
        ping = int(ping_in_ms) if ping_in_ms is not None else "LOSS"
        f.write(f"{current_timestamp},{server_url},{ping}\n")


def get_server_url() -> str:
    if type(TEST_SERVER_URL) is list:
        random_index = random.randint(0, len(TEST_SERVER_URL) - 1)
        return TEST_SERVER_URL[random_index]
    return TEST_SERVER_URL


def main():
    init_logger()

    while(True):
        used_server_url = get_server_url()
        ping_response = ping_server(used_server_url)
        log_response(ping_response, used_server_url)
        time.sleep(PING_INTERVAL_IN_SEC)


if __name__ == "__main__":
    main()
