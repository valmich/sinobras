from django.contrib import admin
from .models import CaracteristicaQuantitativa, CaracteristicaQualitativa, LoteAco, EnsaioMecanico



# Inline para EnsaioMecanico no admin de LoteAco
class EnsaioMecanicoInline(admin.TabularInline):
    model = EnsaioMecanico
    extra = 1  # Quantidade de formulários extra para novos ensaios

# Admin para CaracteristicaQuantitativa
class CaracteristicaQuantitativaAdmin(admin.ModelAdmin):
    list_display = ['descricao', 'unidade', 'limite_inferior', 'limite_superior', 'valor_nominal']
    search_fields = ['descricao']

# Admin para CaracteristicaQualitativa
class CaracteristicaQualitativaAdmin(admin.ModelAdmin):
    list_display = ['descricao', 'justificativa']
    search_fields = ['descricao']

# Admin para LoteAco
class LoteAcoAdmin(admin.ModelAdmin):
    list_display = ['numero_lote', 'data_producao']
    search_fields = ['numero_lote']
    inlines = [EnsaioMecanicoInline]
    # Adicionar ações ou métodos de validação, se necessário

admin.site.register(CaracteristicaQuantitativa, CaracteristicaQuantitativaAdmin)
admin.site.register(CaracteristicaQualitativa, CaracteristicaQualitativaAdmin)
admin.site.register(LoteAco, LoteAcoAdmin)
