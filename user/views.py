from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.shortcuts import redirect
from django.contrib.auth.models import User

def cadastro(request):
    # tratar usuários como unicos, ver se eles existem
    # concertar as outras possibilidades
    
    #redirecionar para a página inicial se o usuário já estiver autenticado
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('password')
        confirmar_senha = request.POST.get('confirm_password')
       
        if len(username.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0 or len(confirmar_senha.strip()) == 0:
            return render(request, 'cadastro.html')
        
        #verificação para ver se o user existe, implementar django messages para dar o aviso
        if User.objects.filter(username=username).exists():
            return render(request, 'cadastro.html')
        
        if len(senha) >= 6 and senha == confirmar_senha:
            try:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=senha
                )
                print('Usuário criado com sucesso')
            except:
                print('Erro ao criar o user')
            
            #return redirect('/auth/logar')
    
    return render(request, 'cadastro.html')

def logar(request):
    if request.user.is_authenticated:
        return redirect('/')  

    if request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('password')
        
        user = authenticate(request, username=username, password=senha)
        
        if user is not None:
            login(request, user)
            return redirect('/')
        
    return render(request, 'login.html')

def sair(request):
    if request.user.is_authenticated:
        logout(request)
        
    return redirect('/')
    