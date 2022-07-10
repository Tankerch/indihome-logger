import datetime
import os
import pythonping
import time

# CONSTANTS VALUE
OUTPUT_PATH = "output/results.csv"
TEST_SERVER_URL = "1.1.1.1"
PING_INTERVAL_IN_SEC = 1
USING_LOCAL_DATETIME = False
# END CONSTANTS VALUE


def get_output_filename() -> str:
    pass


def init_logger():
    file_open_mode = "a+"
    if os.path.exists(OUTPUT_PATH):
        file_open_mode = "r+"

    with open(OUTPUT_PATH, file_open_mode) as f:
        f.seek(0)
        f.write("timestamp,server,res_time_ms\n")


def ping_server() -> int | None:
    response = pythonping.ping(TEST_SERVER_URL, timeout=3, count=1)
    if response .packets_lost > 0.5:
        return None
    return response.rtt_avg_ms


def log_response(ping_in_ms: int | None):
    current_datetime = datetime.datetime.now() if USING_LOCAL_DATETIME else datetime.datetime.utcnow()
    current_timestamp = int(current_datetime.timestamp())

    with open(OUTPUT_PATH, 'a') as f:
        ping = int(ping_in_ms) if ping_in_ms is not None else "LOSS"
        f.write(f"{current_timestamp},{TEST_SERVER_URL},{ping}\n")


def main():
    init_logger()

    while(True):
        ping_response = ping_server()
        log_response(ping_response)
        time.sleep(PING_INTERVAL_IN_SEC)


if __name__ == "__main__":
    main()
