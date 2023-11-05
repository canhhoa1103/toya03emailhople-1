#region debai
"""
--- ma debai / id
get_name_in_email(email_list)

--- nopbai
00 fork tu bainopmau tren replit tu trang web duoiday 
   https://replit.com/@NamG1/toya03emailhople

01 lam bai vao tep s00_bailam.py, chay Run de co ketqua tatca la 1
02a tao github repo, mo trinhduyetweb de kiemtra tep s00_bailam.py, va lay diachi/url aka githubbailamurl

02b dán diachi githubbailamurl theo mẫu ở trang web duoiday
    https://forms.gle/ZwjSxkx9mEqhL8mj6

--- debai / problem
Viết hàm 
  get_name_in_email(email_list)
trả về tên tài khoản trong email 
Nếu email không hợp lệ, trả về 'ERROR invaid email'

--- vidu mau / testcase
Khi chay voi input                                        | Ketqua output
--------------------------------------------------------- | -----------------
get_name_in_email(['ai-btx@gmail.com'])                   | ['ai-btx']
get_name_in_email(['user1@gmail.com', 'user2@gmail.com']) | ['user1', 'user2']
get_name_in_email([])                                     | []
get_name_in_email(['abb#ccc'])                            | ['ERROR invaid email']
get_name_in_email([None])                                 | ['ERROR invaid email']
get_name_in_email([None, 'abb#ccc'])                      | ['ERROR invaid email', 'ERROR invaid email']
"""
#endregion debai

#region bailam
import re


def get_name_in_email(email_list):
  email_pattern = r'^[a-zA-Z0-9._%+-]+@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})$'
  kq = []
  for email in email_list:
    email = str(email)
    match = re.match(email_pattern, email)
    if email == 'None':
      result = "ERROR invaid email"
      kq.append(f"{result}")
    elif match:
      username = email.split('@')[0]
      kq.append(f"{username}")
    else:
      result = 'ERROR invaid email'
      kq.append(f"{result}")
  return (kq)


get_name_in_email(['ai-btx@gmail.com'])
get_name_in_email(['user1@gmail.com', 'user2@gmail.com'])
get_name_in_email([])
get_name_in_email(['abb#ccc'])
get_name_in_email([None])
get_name_in_email([None, 'abb#ccc'])

if __name__ == '__main__':
  pass
