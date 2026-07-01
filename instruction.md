There is an Apache-style access log available at /app/access.log.

Analyze the log and generate a JSON report at /app/report.json.

The report must include:

1. The total number of requests.
2. The number of unique client IP addresses.
3. The most frequently requested path.

The report should contain valid JSON and use the following keys:

- total_requests
- unique_ips
- top_path
