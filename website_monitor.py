#!/usr/bin/env python3
"""
DarkBoss1BD - Advanced Website Monitoring Tool
Professional monitoring tool with hacker-style interface
No external modules required - Pure Python
"""

import urllib.request
import urllib.error
import time
import threading
import sys
import os
import socket
from datetime import datetime

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

class DarkBossMonitor:
    def __init__(self):
        self.monitoring = False
        self.target_url = ""
        self.check_count = 0
        
    def clear_screen(self):
        """Clear terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_banner(self):
        """Print professional hacker-style banner"""
        banner = f"""
{Colors.GREEN}
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║  {Colors.RED}▓▓▓▓▓ {Colors.WHITE}D A R K B O S S 1 B D   M O N I T O R I N G   T O O L {Colors.RED}▓▓▓▓▓  {Colors.GREEN}║
║                                                                              ║
║  ██████╗  █████╗ ██████╗ ██╗  ██╗██████╗  ██████╗ ███████╗███████╗██████╗   ║
║  ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██╔══██╗██╔════╝ ██╔════╝██╔════╝██╔══██╗  ║
║  ██║  ██║███████║██████╔╝█████╔╝ ██████╔╝██║  ███╗███████╗█████╗  ██║  ██║  ║
║  ██║  ██║██╔══██║██╔══██╗██╔═██╗ ██╔══██╗██║   ██║╚════██║██╔══╝  ██║  ██║  ║
║  ██████╔╝██║  ██║██║  ██║██║  ██╗██████╔╝╚██████╔╝███████║███████╗██████╔╝  ║
║  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚═════╝   ║
║                                                                              ║
╠══════════════════════════════════════════════════════════════════════════════╣
║ {Colors.CYAN}► Telegram ID: {Colors.WHITE}https://t.me/darkvaiadmin                           {Colors.GREEN}║
║ {Colors.CYAN}► Telegram Channel: {Colors.WHITE}https://t.me/windowspremiumkey                 {Colors.GREEN}║
║ {Colors.CYAN}► Hacking/Cracking Website: {Colors.WHITE}https://crackyworld.com/               {Colors.GREEN}║
║ {Colors.YELLOW}► Created by: {Colors.WHITE}Mr. X                                               {Colors.GREEN}║
║ {Colors.MAGENTA}► Version: {Colors.WHITE}2.0 Advanced | Pure Python | No External Modules      {Colors.GREEN}║
╚══════════════════════════════════════════════════════════════════════════════╝
{Colors.RESET}
"""
        print(banner)
    
    def print_status(self, message, status_type="info"):
        """Print status messages with colored output"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        colors = {
            "info": Colors.CYAN,
            "success": Colors.GREEN,
            "warning": Colors.YELLOW,
            "error": Colors.RED,
            "monitor": Colors.MAGENTA,
            "system": Colors.BLUE
        }
        
        color = colors.get(status_type, Colors.WHITE)
        print(f"{Colors.WHITE}[{timestamp}] {color}➜ {message}{Colors.RESET}")
    
    def print_animated_text(self, text, delay=0.05):
        """Print text with typing animation"""
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()
    
    def check_website(self, url):
        """Check website status with advanced error handling"""
        try:
            # Create custom headers
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Connection': 'keep-alive'
            }
            
            start_time = time.time()
            req = urllib.request.Request(url, headers=headers)
            
            with urllib.request.urlopen(req, timeout=10) as response:
                response_time = round((time.time() - start_time) * 1000, 2)
                status_code = response.getcode()
                
                status_colors = {
                    200: Colors.GREEN,
                    301: Colors.YELLOW,
                    302: Colors.YELLOW,
                    404: Colors.RED,
                    500: Colors.RED
                }
                
                color = status_colors.get(status_code, Colors.WHITE)
                
                if status_code == 200:
                    return f"{color}🟢 WEBSITE ACTIVE ✓ | Status: {status_code} | Response: {response_time}ms{Colors.RESET}"
                else:
                    return f"{color}🟡 RESPONSE: {status_code} | Response Time: {response_time}ms{Colors.RESET}"
                
        except urllib.error.HTTPError as e:
            return f"{Colors.YELLOW}🟡 HTTP Error: {e.code} - {e.reason}{Colors.RESET}"
        except urllib.error.URLError as e:
            return f"{Colors.RED}🔴 Connection Failed ✗ | Error: {str(e.reason)}{Colors.RESET}"
        except socket.timeout:
            return f"{Colors.RED}🔴 Connection Timeout ✗ | Server not responding{Colors.RESET}"
        except Exception as e:
            return f"{Colors.RED}🔴 Error: {str(e)}{Colors.RESET}"
    
    def get_ip_info(self, domain):
        """Get IP information for the target domain"""
        try:
            clean_domain = domain.replace('http://', '').replace('https://', '').split('/')[0]
            ip = socket.gethostbyname(clean_domain)
            return ip
        except Exception as e:
            return f"Unable to resolve IP: {str(e)}"
    
    def get_server_info(self, url):
        """Try to get server information"""
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=5) as response:
                server = response.headers.get('Server', 'Unknown')
                return server
        except:
            return "Unknown"
    
    def start_continuous_monitoring(self, target_url, interval=5):
        """Start continuous monitoring"""
        self.monitoring = True
        self.target_url = target_url
        self.check_count = 0
        
        self.clear_screen()
        self.print_banner()
        
        self.print_status(f"🚀 STARTING ADVANCED MONITORING", "monitor")
        self.print_status(f"🎯 Target: {Colors.WHITE}{target_url}{Colors.CYAN}", "monitor")
        self.print_status(f"⏱️  Interval: {Colors.WHITE}{interval}{Colors.CYAN} seconds", "monitor")
        
        # Get target information
        ip_address = self.get_ip_info(target_url)
        server_info = self.get_server_info(target_url)
        
        self.print_status(f"🌐 IP Address: {Colors.WHITE}{ip_address}{Colors.CYAN}", "info")
        self.print_status(f"🖥️  Server: {Colors.WHITE}{server_info}{Colors.CYAN}", "info")
        self.print_status(f"📊 Monitoring started at: {Colors.WHITE}{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Colors.CYAN}", "info")
        
        print(f"\n{Colors.MAGENTA}{'═' * 80}{Colors.RESET}")
        self.print_status("🟢 Monitoring Active - Press Ctrl+C to stop", "success")
        print(f"{Colors.MAGENTA}{'═' * 80}{Colors.RESET}\n")
        
        try:
            while self.monitoring:
                self.check_count += 1
                status = self.check_website(target_url)
                timestamp = datetime.now().strftime("%H:%M:%S")
                print(f"{Colors.WHITE}[{timestamp}] {Colors.CYAN}[#{self.check_count:04d}] {status}")
                time.sleep(interval)
                
        except KeyboardInterrupt:
            self.stop_monitoring()
    
    def stop_monitoring(self):
        """Stop monitoring"""
        self.monitoring = False
        print(f"\n{Colors.MAGENTA}{'═' * 80}{Colors.RESET}")
        self.print_status(f"🛑 Monitoring Stopped", "warning")
        self.print_status(f"📈 Total checks performed: {Colors.WHITE}{self.check_count}{Colors.YELLOW}", "warning")
        self.print_status(f"⏰ Session ended at: {Colors.WHITE}{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Colors.YELLOW}", "warning")
        print(f"{Colors.MAGENTA}{'═' * 80}{Colors.RESET}")
    
    def single_website_check(self, target_url):
        """Perform a single comprehensive website check"""
        self.clear_screen()
        self.print_banner()
        
        self.print_status(f"🔍 PERFORMING COMPREHENSIVE WEBSITE CHECK", "system")
        self.print_status(f"🎯 Target: {Colors.WHITE}{target_url}{Colors.BLUE}", "system")
        
        print(f"\n{Colors.CYAN}{'─' * 60}{Colors.RESET}")
        
        # Get comprehensive information
        ip_address = self.get_ip_info(target_url)
        server_info = self.get_server_info(target_url)
        
        self.print_status(f"🌐 IP Resolution: {Colors.WHITE}{ip_address}{Colors.CYAN}", "info")
        self.print_status(f"🖥️  Server Info: {Colors.WHITE}{server_info}{Colors.CYAN}", "info")
        
        print(f"{Colors.CYAN}{'─' * 60}{Colors.RESET}")
        
        # Perform multiple rapid checks
        self.print_status("🚀 Performing rapid connectivity tests...", "monitor")
        
        for i in range(3):
            status = self.check_website(target_url)
            timestamp = datetime.now().strftime("%H:%M:%S")
            print(f"{Colors.WHITE}[{timestamp}] {Colors.MAGENTA}[Test {i+1}] {status}")
            if i < 2:  # Don't sleep after last check
                time.sleep(1)
        
        print(f"{Colors.CYAN}{'─' * 60}{Colors.RESET}")
        self.print_status("✅ Comprehensive check completed", "success")
    
    def show_loading_animation(self, duration=3):
        """Show loading animation"""
        animation = "⣾⣽⣻⢿⡿⣟⣯⣷"
        start_time = time.time()
        i = 0
        
        while time.time() - start_time < duration:
            print(f"\r{Colors.CYAN}Initializing DarkBoss System {animation[i % len(animation)]}{Colors.RESET}", end='')
            time.sleep(0.1)
            i += 1
        
        print("\r" + " " * 50 + "\r", end='')
    
    def run(self):
        """Main application loop"""
        self.clear_screen()
        self.show_loading_animation(2)
        self.print_banner()
        
        while True:
            try:
                print(f"\n{Colors.YELLOW}{Colors.BOLD}🔧 MAIN MENU:{Colors.RESET}")
                print(f"{Colors.CYAN}┌─────────────────────────────────────────────┐")
                print(f"│  {Colors.GREEN}1.{Colors.WHITE} 🚀 Continuous Website Monitoring        {Colors.CYAN}│")
                print(f"│  {Colors.GREEN}2.{Colors.WHITE} 🔍 Single Website Check                 {Colors.CYAN}│")
                print(f"│  {Colors.GREEN}3.{Colors.WHITE} 🌐 Multiple URL Check                   {Colors.CYAN}│")
                print(f"│  {Colors.GREEN}4.{Colors.WHITE} ❌ Exit Tool                           {Colors.CYAN}│")
                print(f"└─────────────────────────────────────────────┘{Colors.RESET}")
                
                choice = input(f"\n{Colors.GREEN}🎯 Enter your choice ({Colors.WHITE}1-4{Colors.GREEN}): {Colors.RESET}").strip()
                
                if choice == "1":
                    target = input(f"\n{Colors.CYAN}🌐 Enter target URL {Colors.WHITE}(e.g., http://example.com){Colors.CYAN}: {Colors.RESET}").strip()
                    if not target:
                        self.print_status("❌ No URL provided!", "error")
                        continue
                    
                    if not target.startswith(('http://', 'https://')):
                        target = 'http://' + target
                    
                    try:
                        interval_input = input(f"{Colors.CYAN}⏱️  Enter check interval in seconds {Colors.WHITE}(default 5){Colors.CYAN}: {Colors.RESET}").strip()
                        interval = int(interval_input) if interval_input else 5
                        if interval < 1:
                            interval = 5
                    except:
                        interval = 5
                    
                    self.start_continuous_monitoring(target, interval)
                    
                elif choice == "2":
                    target = input(f"\n{Colors.CYAN}🌐 Enter target URL {Colors.WHITE}(e.g., http://example.com){Colors.CYAN}: {Colors.RESET}").strip()
                    if not target:
                        self.print_status("❌ No URL provided!", "error")
                        continue
                    
                    if not target.startswith(('http://', 'https://')):
                        target = 'http://' + target
                    
                    self.single_website_check(target)
                    
                elif choice == "3":
                    self.multiple_url_check()
                    
                elif choice == "4" or choice.lower() == 'exit':
                    self.print_status("👋 Thank you for using DarkBoss1BD Monitoring Tool!", "success")
                    self.print_status("📞 Contact: https://t.me/darkvaiadmin", "info")
                    break
                    
                else:
                    self.print_status("❌ Invalid choice! Please select 1-4", "error")
                    
            except KeyboardInterrupt:
                self.print_status("\n🛑 Tool stopped by user", "warning")
                break
            except Exception as e:
                self.print_status(f"💥 An error occurred: {str(e)}", "error")
    
    def multiple_url_check(self):
        """Check multiple URLs at once"""
        self.clear_screen()
        self.print_banner()
        
        self.print_status("🌐 MULTIPLE URL CHECK MODE", "system")
        self.print_status("Enter URLs one by one (type 'done' when finished)", "info")
        
        urls = []
        while True:
            url = input(f"\n{Colors.CYAN}Enter URL {len(urls)+1} {Colors.WHITE}(or 'done'){Colors.CYAN}: {Colors.RESET}").strip()
            if url.lower() == 'done':
                break
            if url:
                if not url.startswith(('http://', 'https://')):
                    url = 'http://' + url
                urls.append(url)
        
        if not urls:
            self.print_status("❌ No URLs provided!", "error")
            return
        
        self.clear_screen()
        self.print_banner()
        self.print_status(f"🔍 Checking {len(urls)} URLs simultaneously...", "monitor")
        print()
        
        for url in urls:
            status = self.check_website(url)
            print(f"{Colors.WHITE}🎯 {url}")
            print(f"   {status}\n")

def main():
    """Main function"""
    try:
        # Check if system supports colors
        if os.name == 'nt':
            os.system('color')
        
        monitor = DarkBossMonitor()
        monitor.run()
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}🔴 Program terminated by user{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.RED}💥 Critical error: {str(e)}{Colors.RESET}")

if __name__ == "__main__":
    main()
