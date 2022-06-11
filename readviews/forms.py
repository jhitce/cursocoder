from django import forms

class datos_generalesForm (forms.Form):
    titulo = forms.CharField(label='Titulo',max_length=80)
    fecha_inicio = forms.DateField(label='Fecha de inicio',input_formats=["%d/%m/%Y"],
    widget=forms.TextInput(attrs={'placeholder': '¿Cuando empezaste a ver o leer? Respeta el formato "30/12/1995"'}))
    comentarios = forms.CharField(label='Comentarios',max_length=240,widget=forms.TextInput(attrs={'placeholder': 'Me gusto porque me enseño..'}))
    autor = forms.CharField(label='Director o autor', max_length=40,widget=forms.TextInput(attrs={'placeholder': 'Director si es serie o pelicula, autor en caso de ser un libro'}))
    
class seriesForm (datos_generalesForm):
    temporadas = forms.IntegerField(label = 'Temporadas',widget=forms.TextInput(attrs={'placeholder': '¿Cuantas temporadas tiene?'}))
    plataforma = forms.CharField(label = 'Plataforma de reproducción',max_length=20,widget=forms.TextInput(attrs={'placeholder': '¿La viste en Netflix? ¿HBO? Contanos dónde'}))
    fecha_final = forms.DateField(label='Fecha final de visualización',input_formats=["%d/%m/%Y"],widget=forms.TextInput(attrs={'placeholder': '¿Cuando terminaste de verla? Respeta el formato "30/12/1995"'}))

class peliculasForm(datos_generalesForm):
    plataforma = forms.CharField(label = 'Plataforma de reproducción',max_length=20,widget=forms.TextInput(attrs={'placeholder': '¿La viste en Netflix? ¿HBO? Contanos dónde'}))
    genero = forms.CharField(label='Genero',max_length=15,widget=forms.TextInput(attrs={'placeholder': 'Terror / Suspenso / Acción ..'}))
    
class librosForm(datos_generalesForm):
    fecha_final = forms.DateField(label='Fecha final de lectura',input_formats=["%d/%m/%Y"],widget=forms.TextInput(attrs={'placeholder': '¿Cuando terminaste de leerlo? Respeta el formato "30/12/1995"'}))
    genero = forms.CharField(label='genero',max_length=25,widget=forms.TextInput(attrs={'placeholder': 'Novela / Divulgación cientifica / Autoayuda..'}))

class BuscarPeliculaForm(forms.Form):
    palabra_a_buscar = forms.CharField(label='Titulo',max_length=80)

class BuscarSerieForm(forms.Form):
    palabra_a_buscar = forms.CharField(label='Titulo',max_length=80)

class BuscarLibroForm(forms.Form):
    palabra_a_buscar = forms.CharField(label='Titulo',max_length=80)

