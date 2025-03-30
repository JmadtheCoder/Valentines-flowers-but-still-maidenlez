#include <iostream> #include <string>

int main() { std::cout << "Welcome to the Computer Dictionary by JmadTheCoder!\n\n"; std::cout << "Enter a term to learn about it (or type EXIT to quit):\n\n"; std::cout << "Input Devices:\n"; std::cout << "1. Keyboard\n2. Mouse\n3. Scanner\n4. Microphone\n5. Webcam\n\n"; std::cout << "Output Devices:\n"; std::cout << "1. Monitor\n2. Printer\n3. Speaker\n4. Plotter\n\n"; std::cout << "Storage Devices:\n"; std::cout << "1. Hard Disk Drive\n2. Solid-State Drive\n3. Flash Drive\n\n"; std::cout << "Computer Types:\n"; std::cout << "1. Microcomputers\n2. Minicomputers\n3. Mainframe Computers\n4. Supercomputers\n\n"; std::cout << "Software:\n"; std::cout << "1. System Software\n2. Application Software\n\n"; std::cout << "Security:\n"; std::cout << "1. SECURITY\n2. HACKER\n3. CRACKER\n\n"; std::cout << "Basic Computing Concepts:\n"; std::cout << "1. BOOTING UP\n2. LOGGING IN\n3. RUNNING PROGRAMS\n4. ACCESSING DATA\n5. CONNECTING TO THE INTERNET\n6. COMMUNICATE WITH OTHER DEVICES\n7. SAVING AND BACKING UP\n8. SHUTTING DOWN\n9. TROUBLESHOOTING\n10. MULTITASKING\n11. SPEED\n\n"; std::cout << "Computer History:\n"; std::cout << "1. NAPIER'S BONES\n2. INTRODUCTION TO COMPUTERS\n\n";

while (true) {
    std::cout << "Enter a Term: ";
    std::string input;
    std::getline(std::cin, input);
    
    if (input == "EXIT") {
        std::cout << "Exiting program.\n";
        break;
    } else if (input == "SECURITY") {
        std::cout << "It's important to keep your computer secure by using antivirus software, firewalls, and other security measures.\n";
    } else if (input == "TROUBLESHOOTING") {
        std::cout << "If you experience issues with your computer, you may need to troubleshoot the problem.\n";
    } else if (input == "SHUTTING DOWN") {
        std::cout << "When you're finished using your computer, you should shut it down properly.\n";
    } else if (input == "SAVING AND BACKING UP") {
        std::cout << "It's important to save and back up your data regularly to avoid data loss.\n";
    } else if (input == "COMMUNICATE WITH OTHER DEVICES") {
        std::cout << "You can communicate with other devices connected to your computer, such as printers, scanners, or other peripherals.\n";
    } else if (input == "CONNECTING TO THE INTERNET") {
        std::cout << "You can connect to the internet to access websites, download files, and communicate with others online.\n";
    } else if (input == "ACCESSING DATA") {
        std::cout << "You can access data stored on your computer or other connected devices, such as external hard drives or cloud storage services.\n";
    } else if (input == "RUNNING PROGRAMS") {
        std::cout << "Once you have logged in, you can run programs on your computer.\n";
    } else if (input == "LOGGING IN") {
        std::cout << "After booting up, you will need to log in to access your user account.\n";
    } else if (input == "BOOTING UP") {
        std::cout << "This is the process of starting up the computer by loading the Operating System (OS).\n";
    } else if (input == "MULTITASKING") {
        std::cout << "Multitasking is one of the main advantages of computers. A person can do multiple tasks and multiple operations at the same time.\n";
    } else if (input == "SPEED") {
        std::cout << "One of the most important advantages of computers is their incredible speed, which helps humans finish tasks in a few seconds.\n";
    } else if (input == "NAPIER'S BONES") {
        std::cout << "It is a manually operated calculating device invented by John Napier.\n";
    } else if (input == "HACKER") {
        std::cout << "A person who explores and learns about computer systems, often with permission.\n";
    } else if (input == "CRACKER") {
        std::cout << "A person who breaks into computer systems without permission, often with malicious intent.\n";
    } else if (input == "INTRODUCTION TO COMPUTERS") {
        std::cout << "Electronic devices that accept data, process it, and produce output. Uses include communication, education, entertainment, and business.\n";
    } else if (input == "MICROCOMPUTERS") {
        std::cout << "Personal computers, laptops, and mobile devices.\n";
    } else if (input == "MINICOMPUTERS") {
        std::cout << "Mid-range computers for small businesses and organizations.\n";
    } else if (input == "MAINFRAME COMPUTERS") {
        std::cout << "Large computers for big businesses, governments, and institutions.\n";
    } else if (input == "SUPERCOMPUTERS") {
        std::cout << "High-performance computers for scientific research and simulations.\n";
    } else if (input == "INPUT DEVICES") {
        std::cout << "Keyboard, mouse, scanner, microphone, and webcam.\n";
    } else if (input == "OUTPUT DEVICES") {
        std::cout << "Monitor, printer, speaker, and plotter.\n";
    } else {
        std::cout << "Term not found in the dictionary. Try again.\n";
    }
}
return 0;

}

