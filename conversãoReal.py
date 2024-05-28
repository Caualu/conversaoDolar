import dearpygui.dearpygui as dpg

dpg.create_context()


def Conversao():
    #função que será chamada quando o usuário clicar no botão de calcular 
  opcao = dpg.get_value("opcao")
  moeda = dpg.get_value("moeda")
  try:
      #converter os valores obtidos para os tipos numéricos adequados
    opcao = int(opcao)
    moeda = float(moeda)
    if opcao == 1:
      resultado = moeda / 5.17
      dpg.set_value("resultado", f" Conversao final:${resultado:,.2f}")
    elif opcao == 2:
      resultado = 5.17 * moeda
      dpg.set_value("resultado", f" Conversao final:${resultado:,.2f}")
    else:
      dpg.set_value("resultado", "por favor, insira valores numerico validos")         
        
  except ValueError:
    dpg.set_value("resultado", "Erro: Por favor, insira valores numéricos válidos")

dpg.create_viewport(title='Calculadora de Conversao', width=700, height=300)
with dpg.window(label="Calculadora Conversão", width=600, height=300):
  
  dpg.add_text("qual opcao voce quer \nReal/Dolar Digite - 1 \nDolar/Dolar digite - 2:")
    
  dpg.add_input_text(label="opcao:", tag="opcao")
    
  dpg.add_input_text(label="Real/Dolar:", tag="moeda")

  dpg.add_button(label="Calcular Conversão", callback=Conversao)
  dpg.add_text("", tag="resultado")


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()