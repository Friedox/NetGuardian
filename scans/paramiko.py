import paramiko


async def perform_scan():
    # Connect to an SSH server and attempt authentication
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect('example.com', username='username', password='password')
        return "SSH connection successful"
    except paramiko.AuthenticationException:
        return "Authentication failed"
    except paramiko.SSHException as e:
        return f"SSH connection failed: {str(e)}"
