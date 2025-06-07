import tkinter as tk
import time

# ---------------------------- CONFIGURATION ------------------------------- #
STUDY_TIME = 50 * 60  # 50 minutes in seconds
BREAK_TIME = 10 * 60  # 10 minutes in seconds
TOTAL_SESSIONS = 10

current_session = 1
is_break = False
timer_running = False

# ---------------------------- TIMER FUNCTION ------------------------------- #
def start_timer():
    global current_session, is_break, timer_running

    if current_session > TOTAL_SESSIONS:
        session_label.config(text="🎉 All Sessions Complete!", fg="#7FDBFF")
        return

    if not timer_running:
        timer_running = True
        session_type = "Break Time 🧘" if is_break else "Study Time 📖"
        session_label.config(text=f"{session_type} (Session {current_session}/{TOTAL_SESSIONS})")
        count_down(BREAK_TIME if is_break else STUDY_TIME)

# ---------------------------- COUNTDOWN FUNCTION -------------------------- #
def count_down(count):
    minutes = count // 60
    seconds = count % 60
    timer_display.config(text=f"{minutes:02d}:{seconds:02d}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        global is_break, current_session, timer_running
        if is_break:
            current_session += 1
        is_break = not is_break
        timer_running = False
        start_timer()

# ---------------------------- UI SETUP ------------------------------------ #
window = tk.Tk()
window.title("Pomodoro Timer - Study With Me")
window.geometry("500x400")
window.configure(bg="#1e1e2f")

# Custom Fonts
FONT_LARGE = ("Courier New", 48, "bold")
FONT_MEDIUM = ("Segoe UI", 20, "bold")
FONT_SMALL = ("Segoe UI", 14)

# Title
title_label = tk.Label(window, text="Pomodoro Study Timer", font=FONT_MEDIUM,
                       fg="#ffffff", bg="#1e1e2f")
title_label.pack(pady=10)

# Session Label
session_label = tk.Label(window, text="Session 1/10", font=FONT_SMALL,
                         fg="#7FDBFF", bg="#1e1e2f")
session_label.pack(pady=5)

# Timer Display
timer_display = tk.Label(window, text="50:00", font=FONT_LARGE,
                         fg="#FF6F61", bg="#1e1e2f")
timer_display.pack(pady=20)

# Start Button
start_btn = tk.Button(window, text="Start Timer", command=start_timer,
                      font=FONT_MEDIUM, bg="#333", fg="#00D1FF",
                      activebackground="#444", activeforeground="#ffffff",
                      relief="flat", padx=20, pady=10)
start_btn.pack(pady=20)

# Footer
footer = tk.Label(window, text="Developed by Ranker Study NEET", font=FONT_SMALL,
                  fg="#888", bg="#1e1e2f")
footer.pack(side="bottom", pady=10)

window.mainloop()
