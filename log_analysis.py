# Sample authentication log analysis tool

logs = [
    "2026-01-10 08:15:23,jsmith,LOGIN_SUCCESS",
    "2026-01-10 08:17:01,mbrown,LOGIN_FAILED",
    "2026-01-10 08:17:45,mbrown,LOGIN_FAILED",
    "2026-01-10 08:18:10,mbrown,LOGIN_FAILED",
    "2026-01-10 09:02:14,adoe,LOGIN_SUCCESS",
    "2026-01-10 09:10:55,jsmith,LOGIN_FAILED",
    "2026-01-10 09:11:20,jsmith,LOGIN_FAILED",
    "2026-01-10 09:12:03,jsmith,LOGIN_FAILED",
    "2026-01-10 10:05:44,admin,LOGIN_SUCCESS"
]

failed_logins = {}

for entry in logs:
    timestamp, username, status = entry.split(",")

    if status == "LOGIN_FAILED":
        if username in failed_logins:
            failed_logins[username] += 1
        else:
            failed_logins[username] = 1

print("Failed Login Summary:")
for username, count in failed_logins.items():
    print(f"{username}: {count} failed login attempts")

print("\nSuspicious Activity:")
for username, count in failed_logins.items():
    if count >= 3:
        print(f"ALERT: {username} has {count} failed login attempts")