# Seminar Notification Calendar Tool

Welcome to the **Seminar Notification Calendar Tool**! 🎓📅

TL:DR:
subscribe to this URL: https://raw.githubusercontent.com/fnyin/berlin-seminar-cal/main/berlin_econ_seminar_calendar.ics

This project collects the latest seminar listings from the university or research group website, generates a `.ics` calendar file, and hosts it on GitHub so you can **subscribe** directly to the calendar in Google Calendar, Apple Calendar, or any other calendar app that supports `.ics` subscriptions.

Currently, it only contains information of BQSE and BAMS seminar series, but expanding!
On my list: Econ History, Development

Alternatively, you can use it as a template to scrape any seminar series by modifying the scraping logic. Note that you will have to add the info.py script yourself (with the URL, time ... etc).

---

### 🌟 What This Tool Does

✅ Automates scraping seminar schedules from the webpage
✅ Builds an `.ics` calendar feed you can subscribe to
✅ Avoids manually checking seminar websites for every update
✅ Lets you subscribe **once** and get new seminars added to your calendar automatically

---

### ⚠ Important Caveats

* **This scraper is very sensitive to seminar website changes.** If they change the URL, table layout, or data format, the scraper will likely break and need maintenance.
* **Updates to locations or rescheduled seminars may not sync well.** If a seminar changes details after you accepted it in your calendar, the tool might not update it properly. Always double-check the seminar's official website for the latest information.

This tool is mainly designed to save you from repeatedly visiting the seminar page and to automate the addition of new seminars to your calendar. It is **not** a substitute for checking last-minute changes or announcements.

---

### 🔧 How to Use

✅ **Subscribe to the Calendar:**

* Use the GitHub-hosted `.ics` file URL.
* Add it to your Google Calendar, Apple Calendar, or similar.

✅ **No need to run the script locally, unless you want to:**

* Update the seminar list.
* Refresh or fix the scraper after a website change.

---


### 🙏 Maintenance

Please note that **the script needs occasional maintenance**:

* Monitor if the seminar website changes.
* Watch for scraping errors or missing fields.
* Update the script as needed to keep the `.ics` feed working.

If you encounter issues or want to improve the tool, feel free to submit pull requests or open issues on this repository!

email: fan.yin@hu-berlin.de
