// There seems to be some sort-of bug in pyautogui which doesn't register key presses(for me, atleast). So, I'm doing this with c++


#include <Windows.h> // This only works for windows. Will try out on a mac when I get my hands on one.
#include <iostream>
#include <string>
#define WINVER 0x0500 // This needs to be defined for windows version 2000 and later. Pretty sure mine is the latest

// Im'ma define all the key codes so it's easier(boi it's gonna be long!)

#define A 0x41
#define B 0x42
#define C 0x43
#define D 0x44
#define E 0x45
#define F 0x46
#define G 0x47
#define H 0x48
#define I 0x49
#define J 0x4A
#define K 0x4B
#define L 0x4C
#define M 0x4D
#define N 0x4E
#define O 0x4F
#define P 0x50
#define Q 0x51
#define R 0x52
#define S 0x53
#define T 0x54
#define U 0x55
#define V 0x56
#define W 0x57
#define X 0x58
#define Y 0x59
#define Z 0x5A
#define CTRL 0xA2
#define SHIFT 0xA0

std::string GetClipboardText();

int main()
{
    // Create a generic keyboard event structure
    INPUT ip;
    ip.type = INPUT_KEYBOARD;
    ip.ki.wScan = 0;
    ip.ki.time = 0;
    ip.ki.dwExtraInfo = 0;



    // Press the "Ctrl" key
    ip.ki.wVk = CTRL;
    ip.ki.dwFlags = 0; // 0 for key press
    SendInput(1, &ip, sizeof(INPUT));

    // Press the "C" key
    ip.ki.wVk = 'C';
    ip.ki.dwFlags = 0; // 0 for key press
    SendInput(1, &ip, sizeof(INPUT));

    // Release the "C" key
    ip.ki.wVk = 'C';
    ip.ki.dwFlags = KEYEVENTF_KEYUP;
    SendInput(1, &ip, sizeof(INPUT));

    // Release the "Ctrl" key
    ip.ki.wVk = CTRL;
    ip.ki.dwFlags = KEYEVENTF_KEYUP;
    SendInput(1, &ip, sizeof(INPUT));

    std::cout << GetClipboardText() << "\n";

}

std::string GetClipboardText()
{
    
    // Get handle of clipboard object for ANSI text
    HANDLE hData = GetClipboardData(CF_TEXT);

    // Lock the handle to get the actual text pointer
    char* pszText = static_cast<char*>(GlobalLock(hData));
  
    // Save text in a string class instance
    std::string text(pszText);

    // Release the lock
    GlobalUnlock(hData);

    // Release the clipboard
    CloseClipboard();

    return text;
}