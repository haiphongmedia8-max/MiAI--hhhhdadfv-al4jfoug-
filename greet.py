#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MiAI Greeting Application
Simple greeting application in Vietnamese
"""

def greet_user(name=None):
    """
    Greet a user in Vietnamese
    
    Args:
        name (str, optional): Name of the person to greet
    
    Returns:
        str: Greeting message
    """
    if name:
        return f"Chào bạn {name}!"
    else:
        return "Chào bạn!"

def main():
    """Main function to run the greeting application"""
    print("=" * 50)
    print("MiAI - Ứng dụng chào hỏi")
    print("=" * 50)
    
    # Greet without name
    print(greet_user())
    
    # Get user input
    name = input("\nNhập tên của bạn (hoặc Enter để bỏ qua): ").strip()
    
    if name:
        print(f"\n{greet_user(name)}")
        print(f"Rất vui được gặp bạn!")
    else:
        print("\nChào bạn! Chúc bạn một ngày tốt lành!")
    
    print("=" * 50)

if __name__ == "__main__":
    main()
