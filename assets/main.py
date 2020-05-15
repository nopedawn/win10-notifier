# Windows 10 Notifier with win10toast library
from win10toast import ToastNotifier

toast = ToastNotifier()
toast.show_toast("Notification", "Check my Own Github https://github.com/nopedawn", duration=30)