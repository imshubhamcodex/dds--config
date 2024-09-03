# pip install rti.connext
import rti.connextdds as dds
import rti.types as idl
from time import sleep

@idl.struct
class StringWrapper:
    content: str = ""

# Paths of security files
identity_cert_file = "./identity_cert.pem"  
private_key_file = "./private_key.pem"      
permissions_file = "./permissions.xml"      # Path to permissions file
governance_file = "./governance.xml"        # Path to governance file

# Create a security configuration profile
security_qos = dds.DomainParticipantQos()
security_qos << dds.Property(
    {
        "dds.sec.auth.identity_ca": identity_cert_file,
        "dds.sec.auth.private_key": private_key_file,
        "dds.sec.access.permissions": permissions_file,
        "dds.sec.access.governance": governance_file
    }
)

# Create a secure domain participant
participant = dds.DomainParticipant(domain_id=0, qos=security_qos)

# Create a secure topic
topic = dds.Topic(participant, "SecureTopic", StringWrapper)

# Create a secure publisher and data writer
publisher = dds.Publisher(participant)
writer = dds.DataWriter(publisher, topic)

# Publish secure data
msg_counter = 0
while True:
    msg_counter += 1

    # Create an instance of StringWrapper with the content
    message = StringWrapper(content=str(msg_counter) + ". This is a secure message")
    
    # Write the instance to the DataWriter
    writer.write(message)
    print(f"{msg_counter}. Message published successfully.")
    sleep(1)
