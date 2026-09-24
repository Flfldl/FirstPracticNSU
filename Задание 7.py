print( "Для смены пароля введите логин и старый пароль" )
Login = input( "Login" )
Password = input( "Password" )
NewPassword = input( "New Password" )
if Password != NewPassword:
 print( "Вы успешно сменили пароль" )
if Password == NewPassword:
 print( "Новый пароль должен отличаться от старого" )