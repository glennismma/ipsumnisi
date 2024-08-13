def handle_log(status_message):
    if 'unknown' in status_message.lower():
        # Special handling for logs containing 'unknown'
        print("Alert: An unknown status detected!")
    else:
        # Normal log handling
        print("Log processed normally.")

# Example log entries
log_entries = [
    "System status: UNKNOWN",
    "Operation completed successfully.",
    "Error: Unknown user ID",
    "Everything is operational."
]

for log in log_entries:
    handle_log(log)
