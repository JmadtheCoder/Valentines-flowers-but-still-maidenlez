# Dictionary of Computer-Related Terms
DATA = {
    "SECURITY": "It's important to keep your computer secure by using antivirus software, firewalls, and other security measures.",
    "TROUBLESHOOTING": "If you experience issues with your computer, you may need to troubleshoot the problem.",
    "SHUTTING DOWN": "When you're finished using your computer, you should shut it down properly.",
    "SAVING AND BACKING UP": "It's important to save and back up your data regularly to avoid data loss.",
    "COMMUNICATE WITH OTHER DEVICES": "You can communicate with other devices connected to your computer, such as printers, scanners, or other peripherals.",
    "CONNECTING TO THE INTERNET": "You can connect to the internet to access websites, download files, and communicate with others online.",
    "ACCESSING DATA": "You can access data stored on your computer or other connected devices, such as external hard drives or cloud storage services.",
    "RUNNING PROGRAMS": "Once you have logged in, you can run programs on your computer.",
    "LOGGING IN": "After booting up, you will need to log in to access your user account.",
    "BOOTING UP": "This is the process of starting up the computer by loading the Operating System (OS).",
    "MULTITASKING": "Multitasking is one of the main advantages of computers. A person can do multiple tasks and multiple operations at the same time.",
    "SPEED": "One of the most important advantages of computers is their incredible speed, which helps humans finish tasks in a few seconds.",
    "NAPIER'S BONES": "It is a manually operated calculating device invented by John Napier.",
    "HACKER": "A person who explores and learns about computer systems, often with permission.",
    "CRACKER": "A person who breaks into computer systems without permission, often with malicious intent.",
    "INTRODUCTION TO COMPUTERS": "Electronic devices that accept data, process it, and produce output. Uses include communication, education, entertainment, and business.",
    "MICROCOMPUTERS": "Personal computers, laptops, and mobile devices.",
    "MINICOMPUTERS": "Mid-range computers for small businesses and organizations.",
    "MAINFRAME COMPUTERS": "Large computers for big businesses, governments, and institutions.",
    "SUPERCOMPUTERS": "High-performance computers for scientific research and simulations.",
    "INPUT DEVICES": "Keyboard, mouse, scanner, microphone, and webcam.",
    "OUTPUT DEVICES": "Monitor, printer, speaker, and plotter.",
    "STORAGE DEVICES": "Hard disk drive, solid-state drive, and flash drive.",
    "RAM": "Random Access Memory - Temporary storage for data and applications.",
    "HARD DISK": "Permanent storage for data, programs, and operating systems.",
    "SYSTEM SOFTWARE": "Includes operating systems, device drivers, and utilities.",
    "APPLICATION SOFTWARE": "Includes productivity software, games, and multimedia applications.",
    "PROGRAMMING SOFTWARE": "Includes compilers, interpreters, and development tools.",
    "BASIC COMPUTER OPERATIONS": "Includes input (data entry), processing (CPU work), storage (memory or storage devices), and output (display results).",
    "HARDWARE FAILURE": "Faulty or damaged hardware components.",
    "SOFTWARE BUGS": "Errors or flaws in software programs.",
    "USER ERROR": "Mistakes or incorrect usage by users.",
    "DEPENDENCE ON ELECTRICITY": "Computers require power to operate.",
    "VULNERABILITY TO VIRUSES": "Computers can be infected by malware and viruses.",
    "ENVIRONMENTAL IMPACT": "Computers contribute to e-waste and pollution.",
    "ACCURACY": "Computers perform calculations and operations with high precision.",
    "RELIABILITY": "Computers can operate continuously without fatigue.",
    "VERSATILITY": "Computers can perform a wide range of tasks and operations."
}

print("Welcome to the Computer Dictionary by JmadTheCoder!")
print("Type 'EXIT' to stop.\n")

while True:
    a = input("Enter a computer-related term: ").strip().upper()
    print("\n", DATA.get(a, "Term not found. Try another one."), "\n")