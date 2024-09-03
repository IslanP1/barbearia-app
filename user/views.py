from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages

def cadastrar(request):
    if request.user.is_authenticated:  
        messages.warning(request, 'Usuário autenticado!')
        return redirect('/')
    
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('password')
        confirmar_senha = request.POST.get('confirm_password')
        if len(username.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0 or len(confirmar_senha.strip()) == 0:
            messages.warning(request, 'Preencha os campos!')
            return redirect('/auth/cadastrar/')
        
        #verificação para ver se o user existe, implementar django messages para dar o aviso
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Usuário já existente, coloque outro nome')
            return redirect('/auth/cadastrar/')
        
        if senha == confirmar_senha:
            try:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=senha
                )
                messages.success(request, 'Usuário criado com sucesso!')
                return redirect('/auth/logar/')
            except:
                messages.error(request, 'Erro ao criar o user')
                return redirect('/auth/cadastrar')
        else:
            messages.error(request, 'Digite a mesma senha nos dois campos!')
            return redirect('/auth/cadastrar/')
    
    return render(request, 'cadastro.html')

def logar(request):
    if request.user.is_authenticated:
        messages.warning(request, 'Usuário autenticado!')
        return redirect('/')  

    if request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('password')
        
        user = authenticate(request, username=username, password=senha)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Usuário logado com sucesso!')
            return redirect('/')
        else:
            messages.error(request, 'Usuário ou senha incorretos')
            return redirect('/auth/logar/')
        
    return render(request, 'login.html')

def sair(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'Usuário deslogado com sucesso!')
        return redirect('/')
        
    messages.warning(request, 'Nenhum user logado!')
    return redirect('/')