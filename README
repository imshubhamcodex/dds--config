# RTI Connext DDS Setup Instructions

## Optional Steps (for RTI Trial Version)

1. **Install OpenSSL:**
   - Download the OpenSSL installer from [SLProweb](https://slproweb.com/products/Win32OpenSSL.html).
   - Add the `bin` directory of the OpenSSL installation to the system `PATH` environment variable.

2. **Generate Security Certificates:**
   - To create a private key, run:
     ```bash
     openssl genpkey -algorithm RSA -out private_key.pem -aes256
     ```
   - To create an SSL certificate, run:
     ```bash
     openssl req -new -x509 -key private_key.pem -out identity_cert.pem -days 365
     ```
   - During the certificate creation process, make a note of the `CN` (Common Name), which will be used later in the `permissions.xml` file.

## Additional Steps

3. **Download RTI Connext SDK (Optional):**
   - Download the RTI Connext SDK from [RTI's Free Trial Page](https://www.rti.com/free-trial) if you need the RTI libraries.

4. **Obtain and Configure the License File:**
   - Download the license file from your email and save it in the directory where your application will run.

5. **Update Governance Configuration:**
   - Add the `<domain_participant_qos>` section to your `governance.xml` file.

6. **Refer to Official Documentation:**
   - For more detailed information, refer to the [RTI Connext DDS Python documentation](https://github.com/rticommunity/connextdds-py?tab=readme-ov-file).
