# Iterators and Generators in Python

## ثبت نام
شما میتوانید از [اینجا](#) در دوره ثبت نام کنید.

## دسترسی به فایل ها
تمامی فایل های تمرین، در این مخزن قابل دسترسی هستند. مطالب دسته بندی شدند و فایل ها در بخش های مربوطه آپلود شدند. برای دسترسی، بخش مورد نظر رو انتخاب کنید و به فایل ها دسترسی پیدا کنید.

همچنین میتونید فایل های تمرین رو در قالب یک فایل zip به این صورت دانلود کنید:
```
curl -o exercise_files.zip https://raw.githubusercontent.com/mimseyedi/Iterators_and_Generators_Course/master/exercise_files.zip
```

## فهرست مطالب

* مقدمه
  * آشنایی اولیه با Iterator ها و Generator ها
  * فرآیند Iteration در پایتون
  * آشنایی اولیه با Iterable ها
* Iterator ها
  * پیاده سازی Iterator ها
  * بررسی و پیاده سازی حلقه‌ی For
  * تابع iter
  * تابع next
* انواع Iterator ها
  * کلاسیک
  * مبدل
  * مولد
* Generator ها
  * پیاده سازی Generator ها
  * انواع Generator ها
  * Generator expression
  * بررسی و رصد اجرای Generator ها در پایتون
* متدهای Generator
  * متد send
  * متد throw
  * متد close
* کوروتین های Generator-based
  * مقدمه ای بر مدل های اجرا
  * دستور yield from
  * پیاده سازی Coroutine ها
  * آبجکت های Async
* پردازش بهینه‌ی داده ها
  * مقایسه‌ی Iterator ها و Container ها
  * Pipeline ها
* ماژول itertools
  * Iterator های بینهایت
    * count
    * cycle
    * repeat
  * Iterator های پایان پذیر
    * chain
    * accumulate
    * compress
    * filterfalse
    * dropwhile
    * takewhile
    * starmap
    * islice
    * batched
    * zip_longest
    * pairwise
  * Iterator های ترکیباتی
  * Recipe های ماژول itertools
* مباحث تکمیلی
  * محدودیت های Iterator ها
  * مقایسه‌ی Iterator ها با Iterable ها
  * آبجکت های Reversible
  * ماژول more-itertools