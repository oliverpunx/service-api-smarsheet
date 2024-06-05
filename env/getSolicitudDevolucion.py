import smartsheet
import cx_Oracle
import connect
from datetime import datetime
from datetime import date

SHEETS = 'https://api.smartsheet.com/2.0/sheets'

smartsheet_client = smartsheet.Smartsheet('X8qvLmK1bRbwPE9cgfjZHwe73CpV9FaJ5KwFF')
smartsheet_client.assume_user("miguel.lopez@lhenriques.com")

sheet = smartsheet_client.Sheets.get_sheet("8768078573686660")  #HOJA SOLICITUDES DE DEVOLUCIONES
#3409964803510148 correo electronico cliente
#7860787872747396 id solicitud
#8986687779590020 solicitante
#6734887965904772 fecha registro
#7069139500748676 fecha solicitud
#4535864710352772 division comercial
camposDatetime =["734887965904772","4483088152219524","1158164989824900","6734887965904772","2565539873378180","313740059692932","4817339687063428","7069139500748676","3691439780220804","5380289640484740"]

def cargaSolDevoluciones(miCursor, no_proceso, registro):
    try:
         valores = ""
         sql = ""
         
         for record in registro:
             if record["valor"] != "'null'":
                if record["valor"] == "'True'":
                   valores = valores+"'S',"
                else:
                   if record["valor"] == "'False'":
                      valores = valores+"'N',"
                   else:
                      valores = valores+record["valor"]+","

         valores = valores.strip(",")

         sql = "insert into  tmp_pruebas_smarsheet (no_proceso, id_solicitud, es_urgente, fecha_registro,fecha_solicitud, nombre_solicitante, descripcion_solicitante, codigo_cliente, division_comercial, tipo_solicitud, numero_factura, fecha_factura, correo_vendedor, asignado_a, correo_cliente, estado,motivo_rechazo, guia_servientrega, fecha_recepcion, fecha_envio_guia, fecha_recepcion_est,fecha_ejecucion_estimada, dias_solicitud_vs_registro, estado_tiempo_solicitud, fecha_max_resp_cliente,estado_fecmaxresp_cliente, dias_estimados_ejecucion, fecha_ejecucion,dias_reales_ejecucion, medidas_tomadas,problemas_encontrados, resolucion) values (" + str(no_proceso) + ", " + valores + ")"
         
         print(sql)
         
         miCursor.execute(sql)
         print()
         print("registro insertado exitosamente.")
         print()
         
    except Exception as error:
           print("OCURRIO UN ERROR en cargaSolDevoluciones: "+str(error))


def listaColumnas():
    data = {}
    data['columnas'] = []

    for i in range(0,len(sheet.columns)):
        if sheet.columns[i].id != "":
           #print(sheet.columns[i].id,sheet.columns[i].title,sep=" - ")
           data['columnas'].append({'id': sheet.columns[i].id, "title": sheet.columns[i].title})

    return data['columnas']

def buscaNomColumna(id):
    nombre = ""

    for listaColumnas in dictColumnas:
        if id  == listaColumnas["id"]:
           nombre = listaColumnas["title"]

           break          
     
    return '"' + nombre + '"'

def esFecha(id):
    nombre = ""
    es_fecha = False

    for listaColumnas in dictColumnas:
        if id  == listaColumnas["id"]:
           for i in range(0, len(camposDatetime)):
               if str(listaColumnas["id"]) == str(camposDatetime[i]):
                  es_fecha = True

           break          
     
    return es_fecha    

dictColumnas = listaColumnas()
contador = 0

#print(dictColumnas)

#abro conexion a Oracle
conectorOracle=connect.Conexion()
miConector=conectorOracle.conectaOracle()

solicitudes = {}
solicitudes['lista'] = []
no_proceso = 1

def cadenaaTime(fecha):
    newFecha = ""

    for i in range (0,len(fecha)):
        caracter = fecha[i]

        if caracter.isalpha():
           newFecha = newFecha + " "
        else:
           newFecha = newFecha + caracter

    newFecha = newFecha.strip(" ")

    fecha = newFecha
    newFecha=""

    for i in range (0,len(fecha)):
        caracter = fecha[i]

        if caracter=='-':
           newFecha = newFecha + "/"
        else:
           newFecha = newFecha + caracter
    
    anio = newFecha[0:4]
    mes = newFecha[5:7]
    dia = newFecha[8:10]
    hora = newFecha[11:]
    
    if hora == "":
       newFecha = "to_date('"+dia+"/"+mes+"/"+anio+" "+hora+"','dd/mm/yyyy hh24:mi:ss')"
    else:
       newFecha = "to_date('"+dia+"/"+mes+"/"+anio+"','dd/mm/yyyy')"

    #print(newFecha)

    return newFecha

#fecha="2024-01-15T14:34:12Z"
#newFecha = cadenaaTime(fecha)
#print("**"+newFecha+"**")

#print(str(0)+" -> "+str(sheet.columns[0].id),str(sheet.columns[0].title),sep=" - ")
       
for j in range(0,len(sheet.rows)):
    #print("*****************ROW****************")
    contColumna = 0
    fila = ""
    no_inserta = False

    for k in range(0,len(sheet.rows[j].cells)):
        contColumna += 1
        valor = str(sheet.rows[j].cells[k].value).replace(",","").replace("None","null")
        es_fecha = False
        newFecha = ""

        if valor != '' and valor != "null":
           es_fecha = esFecha(sheet.rows[j].cells[k].column_id)
           nombre = buscaNomColumna(sheet.rows[j].cells[k].column_id)

           try:
               if es_fecha:
                  newFecha = cadenaaTime(valor)
                  valor = newFecha

           except Exception as error:
                  print("Error Conversion de fechas: " + str(error))
                  print()

           finally:
                  if es_fecha:
                     valor = valor
                  else:
                     valor = "'"+valor+"'"
        if (str(sheet.rows[j].cells[k].column_id) == str(sheet.columns[0].id) and (valor == '' or valor == 'null')) :
           no_inserta = True
           fila=""
           solicitudes['lista'].clear()
        
        if no_inserta != True:
           fila = fila + nombre + " = " + valor + ","
           solicitudes['lista'].append({'secuencia': contColumna,'valor': valor})
            
    if (len(solicitudes['lista']))>0:
       cargaSolDevoluciones(miConector.cursor(),no_proceso,solicitudes['lista'])  
       conectorOracle.commitOracle()
    
    solicitudes['lista'].clear()

conectorOracle.closeOracle() 

print("Total de registros: "+str(contador))
