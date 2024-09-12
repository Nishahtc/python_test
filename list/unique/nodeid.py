import uuid

def generate_uuid():
    return str(uuid.uuid4())

# Example usage
node_uuids = [generate_uuid() for _ in range(10)]
print("Generated UUIDs:", node_uuids)