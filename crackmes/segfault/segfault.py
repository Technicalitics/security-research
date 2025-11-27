from pwn import *

attempt = 0
while True:
    # Start process 
    p = process('./a.out')

    # Interact with it 
    p.recvuntil(b'username:\n')
    p.sendline(b'aaaaaaaa')
    p.recvuntil(b'serial number:\n')
    p.sendline(b'12')
    p.recvuntil(b's/n WRONG!')
    
    p.wait()

    # check if segfault
    if p.poll() == -11 or p.poll() == 139:
        print(f"Segfault on attempt {attempt}!")
        output = p.recvall()
        print(output)
        break
    p.close()
