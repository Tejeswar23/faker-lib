from faker import Faker

fake = Faker()
file_path = r"C:\Users\polak\OneDrive\Desktop\faker\faker_project\src\server_log.txt"
status_description = {
    200: "Request processed successfully",
    201: "Resource created successfully",
    400: "Bad request from client",
    401: "Unauthorized access attempt",
    403: "Access forbidden",
    404: "Requested resource not found",
    500: "Internal server error",
    502: "Bad gateway error",
    503: "Service unavailable"
}

with open(file_path, "w") as file:
    for _ in range(10):
        ip = fake.ipv4()
        time = fake.date_time()
        status = fake.random_element(elements=[200, 200, 404, 500, 403])
        level = fake.random_element(elements=['INFO','ERROR','WARNING'])
        status = fake.random_element(elements=list(status_description.keys()))
        description = status_description[status]
        log_line = f'{ip}  {time} "{level}" {status} - {description}\n'
        file.write(log_line)

print("Fake server log generated using Faker.")
