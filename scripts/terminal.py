import os
from datetime import datetime
from zoneinfo import ZoneInfo

# Must be set BEFORE gifos is imported so the library reads them at init
_user = os.environ.get("GH_USER", "pavankumar")
os.environ["GIFOS_GENERAL_USER_NAME"] = _user
os.environ["GIFOS_GENERAL_COLOR_SCHEME"] = "yoru"

import gifos

USER = _user

try:
    stats = gifos.utils.fetch_github_stats(user_name=USER)
except ZeroDivisionError:
    class MockStats:
        account_name = USER
        user_rank = type("Rank", (), {"level": "S+"})()
        total_stargazers = 420
        total_commits_last_year = 1337
        total_pull_requests_made = 69
        pull_requests_merge_percentage = 100.0
        total_repo_contributions = 800
        languages_sorted = [("Python", 100), ("Go", 80), ("TypeScript", 50), ("Rust", 30)]
    stats = MockStats()

FONT_FILE_LOGO = "./fonts/vtks-blocketo.regular.ttf"
FONT_FILE_BITMAP = "./fonts/gohufont-uni-14.pil"
FONT_FILE_MONA = "./fonts/Inversionz.otf"

CUSTOM_PROMPT = f"\x1b[32m{USER}\x1b[0m@\x1b[94mdev\x1b[0m ~> "

def main():
    t = gifos.Terminal(750, 500, 15, 15, FONT_FILE_BITMAP, 15)
    t.set_prompt(CUSTOM_PROMPT)

    t.gen_text("", 1, count=20)
    t.toggle_show_cursor(False)
    year_now = datetime.now(ZoneInfo("Asia/Kolkata")).strftime("%Y")
    t.gen_text("DEV_OS Modular BIOS v2.0.24", 1)
    t.gen_text(f"Copyright (C) {year_now}, \x1b[31mPavanKumar Softwares Inc.\x1b[0m", 2)
    t.gen_text("\x1b[94mAgentic Framework Terminal, Rev 2024\x1b[0m", 4)
    t.gen_text("Neuro(tm) AI_CPU - 1000Hz", 6)
    t.gen_text(
        "Press \x1b[94mDEL\x1b[0m to enter SETUP, \x1b[94mESC\x1b[0m to cancel Memory Test",
        t.num_rows,
    )
    for i in range(0, 256000, 24000):  
        t.delete_row(7)
        if i < 100000:
            t.gen_text(
                f"Memory Test: {i}K", 7, count=2, contin=True
            )  
        else:
            t.gen_text(f"Memory Test: {i}K", 7, contin=True)
    t.delete_row(7)
    t.gen_text("Memory Test: 256MB OK", 7, count=10, contin=True)
    t.gen_text("", 11, count=10, contin=True)

    t.clear_frame()
    t.gen_text("Initiating Boot Sequence ", 1, contin=True)
    t.gen_typing_text(".....", 1, contin=True)
    t.gen_text("\x1b[96m", 1, count=0, contin=True)  
    t.set_font(FONT_FILE_LOGO, 66)
    
    os_logo_text = "WELCOME"
    mid_row = (t.num_rows + 1) // 2
    mid_col = (t.num_cols - len(os_logo_text) + 1) // 2
    effect_lines = gifos.effects.text_scramble_effect_lines(
        os_logo_text, 3, include_special=False
    )
    for i in range(len(effect_lines)):
        t.delete_row(mid_row + 1)
        t.gen_text(effect_lines[i], mid_row + 1, mid_col + 1)


    t.set_font(FONT_FILE_BITMAP, 15)  # restore row/col count before login sequence
    t.set_prompt(CUSTOM_PROMPT)        # font restore also resets prompt; set it again
    t.clear_frame()

    t.clone_frame(5)
    t.toggle_show_cursor(False)
    t.gen_text("\x1b[93mPAVAN OS v2.0.24 (tty1)\x1b[0m", 1, count=5)
    t.gen_text("login: ", 3, count=5)
    t.toggle_show_cursor(True)
    t.gen_typing_text("pavankumar", 3, contin=True)
    t.gen_text("", 4, count=5)
    t.toggle_show_cursor(False)
    t.gen_text("password: ", 4, count=5)
    t.toggle_show_cursor(True)
    t.gen_typing_text("*********", 4, contin=True)
    t.toggle_show_cursor(False)
    time_now = datetime.now(ZoneInfo("Asia/Kolkata")).strftime(
        "%a %b %d %I:%M:%S %p %Z %Y"
    )
    t.gen_text(f"Last login: {time_now} on tty1", 6)

    t.gen_prompt(7, count=5)
    prompt_col = t.curr_col
    t.toggle_show_cursor(True)
    t.gen_typing_text("\x1b[91mclea", 7, contin=True)
    t.delete_row(7, prompt_col)  
    t.gen_text("\x1b[92mclear\x1b[0m", 7, count=3, contin=True)

    t.clear_frame()
    
    user_details_lines = f"""
    \x1b[30;101mpavankumar@GitHub\x1b[0m
    --------------
    \x1b[96mWork:   \x1b[93mFull-stack @ Webbheads\x1b[0m
    \x1b[96mExperience:   \x1b[93mFounding Engineer @ Xentro\x1b[0m
    \x1b[96mStudy:  \x1b[93mB.Tech CSE @ GITAM, class of 2028\x1b[0m
    \x1b[96mFocus:  \x1b[93mAgentic AI, World Models, System Architecture \x1b[0m
    
    \x1b[30;101mProjects:\x1b[0m
    --------------
    \x1b[96mAgentVortex:\x1b[93m Personal AI OS with autonomous agents\x1b[0m
    \x1b[96mMiniGenie:   \x1b[93m Genie world model in PyTorch\x1b[0m
    \x1b[96mAgentAstra:   \x1b[93m Multi-agent startup research platform\x1b[0m
    \x1b[96mSwiftChain:   \x1b[93m Decentralized crypto payments\x1b[0m
    
    \x1b[30;101mTech Stack:\x1b[0m
    --------------
    \x1b[96mLangs:  \x1b[93mPython, C++, TypeScript, JavaScript, SQL\x1b[0m
    \x1b[96mWeb:    \x1b[93mNext.js, FastAPI, Node.js, Tailwind CSS\x1b[0m
    \x1b[96mAI/ML:  \x1b[93mPyTorch, LangGraph, LangChain, TensorFlow\x1b[0m
    \x1b[96mInfra:  \x1b[93mPostgreSQL, Docker, Redis\x1b[0m
    """
    t.gen_prompt(1)
    prompt_col = t.curr_col
    t.clone_frame(10)
    t.toggle_show_cursor(True)
    t.gen_typing_text("\x1b[91mfetch.s", 1, contin=True)
    t.delete_row(1, prompt_col)
    t.gen_text("\x1b[92mfetch.sh\x1b[0m", 1, contin=True)
    t.gen_typing_text(" -u pavankumar", 1, contin=True)

    t.set_font(FONT_FILE_MONA, 16, 0)
    t.toggle_show_cursor(False)
    
    monaLines = r"""
    \x1b[49m     \x1b[90;100m}}\x1b[49m     \x1b[90;100m}}\x1b[0m
    \x1b[49m    \x1b[90;100m}}}}\x1b[49m   \x1b[90;100m}}}}\x1b[0m
    \x1b[49m    \x1b[90;100m}}}}}\x1b[49m \x1b[90;100m}}}}}\x1b[0m
    \x1b[49m   \x1b[90;100m}}}}}}}}}}}}}\x1b[0m
    \x1b[49m   \x1b[90;100m}}}}}}}}}}}}}}\x1b[0m
    \x1b[49m   \x1b[90;100m}}\x1b[37;47m}}}}}}}\x1b[90;100m}}}}}\x1b[0m
    \x1b[49m  \x1b[90;100m}}\x1b[37;47m}}}}}}}}}}\x1b[90;100m}}}\x1b[0m
    \x1b[49m  \x1b[90;100m}}\x1b[37;47m}\x1b[90;100m}\x1b[37;47m}}}}}\x1b[90;100m}\x1b[37;47m}}\x1b[90;100m}}}}\x1b[0m
    \x1b[49m  \x1b[90;100m}\x1b[37;47m}}\x1b[90;100m}\x1b[37;47m}}}}}\x1b[90;100m}\x1b[37;47m}}}\x1b[90;100m}}}\x1b[0m
    \x1b[90;100m}}}\x1b[37;47m}}}}\x1b[90;100m}}}\x1b[37;47m}}}}}\x1b[90;100m}}}}\x1b[0m
    \x1b[49m  \x1b[90;100m}\x1b[37;47m}}}}}\x1b[90;100m}}\x1b[37;47m}}}}}\x1b[90;100m}}}\x1b[0m
    \x1b[49m \x1b[90;100m}}\x1b[37;47m}}}}}}}}}}}}\x1b[90;100m}}}\x1b[0m
    \x1b[90;100m}\x1b[49m  \x1b[90;100m}}\x1b[37;47m}}}}}}}}\x1b[90;100m}}}\x1b[49m  \x1b[90;100m}\x1b[0m
    \x1b[49m        \x1b[90;100m}}}}}\x1b[0m
    \x1b[49m       \x1b[90;100m}}}}}}}\x1b[0m
    \x1b[49m       \x1b[90;100m}}}}}}}}\x1b[0m
    \x1b[49m      \x1b[90;100m}}}}}}}}}}\x1b[0m
    \x1b[49m     \x1b[90;100m}}}}}}}}}}}\x1b[0m
    \x1b[49m     \x1b[90;100m}}}}}}}}}}}}\x1b[0m
    \x1b[49m     \x1b[90;100m}}\x1b[49m \x1b[90;100m}}}}}}\x1b[49m \x1b[90;100m}}\x1b[0m
    \x1b[49m        \x1b[90;100m}}}}}}}\x1b[0m
    \x1b[49m         \x1b[90;100m}}}\x1b[49m \x1b[90;100m}}\x1b[0m
    """
    t.gen_text(monaLines, 10)

    t.set_font(FONT_FILE_BITMAP)
    t.set_prompt(CUSTOM_PROMPT)  # restore after Mona font switch
    t.toggle_show_cursor(True)
    t.gen_text(user_details_lines, 2, 35, count=5, contin=True)
    t.gen_prompt(t.curr_row)
    t.gen_typing_text(
        "\x1b[92m# Pavan's GitHub - Have a nice day! :D",
        t.curr_row,
        contin=True,
    )
    t.gen_text("", t.curr_row, count=80, contin=True)

    t.gen_gif()

if __name__ == "__main__":
    main()
