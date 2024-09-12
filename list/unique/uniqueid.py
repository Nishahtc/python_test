import uuid

# Define a namespace (e.g., URL namespace)
namespace = uuid.NAMESPACE_URL

# Define a name string (e.g., a URL)
name = "https://www.example.com"

# Generate the UUIDv5
v = str(uuid.uuid5(namespace, name))

# Print the first 10 characters of the UUID
print(v[0:10])