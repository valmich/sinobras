from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
import datetime

#Classe abstrata que define o modelo de uma característica de um lote de aço.
class Caracteristica(models.Model):
    descricao = models.CharField(_('Descrição'), max_length=100)

    class Meta:
        abstract = True

    def __str__(self):
        return self.descricao
#Classe que define o modelo de uma característica quantitativa de um lote de aço.
class CaracteristicaQuantitativa(Caracteristica):
    unidade = models.CharField(_('Unidade'), max_length=20)
    limite_inferior = models.DecimalField(_('Limite Inferior'), max_digits=6, decimal_places=3)
    limite_superior = models.DecimalField(_('Limite Superior'), max_digits=6, decimal_places=3)
    valor_nominal = models.DecimalField(_('Valor Nominal'), max_digits=6, decimal_places=3, blank=True, null=True)

    def valor_dentro_limites(self, valor):#Verifica se o valor dado está dentro dos limites da característica.
        return self.limite_inferior <= valor <= self.limite_superior
    
#Classe que define o modelo de uma característica qualitativa de um lote de aço.
class CaracteristicaQualitativa(Caracteristica):
    justificativa = models.BooleanField(_('Justificativa'))

#Classe que define o modelo de um lote de aço.
class LoteAco(models.Model):
    numero_lote = models.CharField(_('Número do Lote'), max_length=20, unique=True)
    data_producao = models.DateField(_('Data de Produção'))
    caracteristicas_quantitativas = models.ManyToManyField(CaracteristicaQuantitativa, verbose_name=_('Características Quantitativas'), blank=True)
    caracteristicas_qualitativas = models.ManyToManyField(CaracteristicaQualitativa, verbose_name=_('Características Qualitativas'), blank=True)

    QUANTIDADE_MINIMA_ENSAIOS = 3 #Constante que define a quantidade mínima de ensaios necessários para avaliar o lote.
    def __str__(self):
        return f"Lote {self.numero_lote} - Produzido em {self.data_producao.strftime('%d/%m/%Y')}"

    def get_ultimos_ensaios(self):
        return self.ensaios.order_by('-data_ensaio')[:self.QUANTIDADE_MINIMA_ENSAIOS]


    #Avalia o lote com base nos ensaios realizados. 
    #Retorna "Pendente" se o lote não possui ensaios suficientes,
    #"Fora de Faixa" se alguma característica quantitativa estiver fora dos limites, ou 
    #"Dentro da Faixa" se todas as características quantitativas estiverem dentro dos limites.
    def avaliar_lote(self): 
        ensaios = self.ensaios.all()
        if ensaios.count() < self.QUANTIDADE_MINIMA_ENSAIOS:
            return "Pendente"

        fora_de_faixa = False
        for caracteristica in CaracteristicaQuantitativa.objects.all():
            valores = [getattr(ensaio, caracteristica.descricao.replace(" ", "_").lower(), None) for ensaio in ensaios]
            valores = [valor for valor in valores if valor is not None]

            if not valores:  # Nenhum valor para esta característica
                continue

            media = sum(valores) / len(valores)
            if not (caracteristica.limite_inferior <= media <= caracteristica.limite_superior):
                fora_de_faixa = True
                break

        return 'Fora de Faixa' if fora_de_faixa else 'Dentro da Faixa'
    
class EnsaioMecanico(models.Model):
    lote = models.ForeignKey(LoteAco, on_delete=models.CASCADE, related_name='ensaios')
    data_ensaio = models.DateField(_('Data do Ensaio'))
    alongamento = models.DecimalField(_('Alongamento (%)'), max_digits=6, decimal_places=3)
    resistencia_escoamento = models.DecimalField(_('Resistência de Escoamento (MPa)'), max_digits=6, decimal_places=3)
    resistencia_ruptura = models.DecimalField(_('Resistência de Ruptura (MPa)'), max_digits=6, decimal_places=3)
    massa_linear = models.DecimalField(_('Massa Linear (Kg/m)'), max_digits=6, decimal_places=3)

    def __str__(self):
        return f"Ensaio do Lote {self.lote.numero_lote} em {self.data_ensaio.strftime('%d/%m/%Y')}"
    
#Valida o ensaio com base nas características quantitativas do lote. 
#Retorna um dicionário com as características quantitativas e o 
#status de cada uma delas ("Valor não fornecido", "Fora dos limites" ou "Dentro dos limites").
    def valida_ensaio(self):
        resultados = {}
        for caracteristica in self.lote.caracteristicas_quantitativas.all():
            campo_ensaio = caracteristica.descricao.replace(" ", "_").lower()
            valor_ensaio = getattr(self, campo_ensaio, None)
            
            if valor_ensaio is None:
                resultados[caracteristica.descricao] = 'Valor não fornecido'
            elif not caracteristica.valor_dentro_limites(valor_ensaio):
                resultados[caracteristica.descricao] = f'Fora dos limites: {valor_ensaio}'
            else:
                resultados[caracteristica.descricao] = 'Dentro dos limites'
        return resultados