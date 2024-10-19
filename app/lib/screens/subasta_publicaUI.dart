// ignore_for_file: file_names

import 'dart:io';

import 'package:app/utils/app_styles.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

class SubastaPublicaUI extends StatefulWidget {
  const SubastaPublicaUI({super.key});

  @override
  _SubastaPublicaUIState createState() => _SubastaPublicaUIState();
}

class _SubastaPublicaUIState extends State<SubastaPublicaUI> {
  String titulo = 'Elige un método';
  String subtitulo = 'Asignaciones de Acciones';
  String hoveredButton = '';
  String pressButton = '';

  // Controladores de texto
  final TextEditingController aController = TextEditingController();
  final TextEditingController bController = TextEditingController();
  final TextEditingController nController = TextEditingController();
  final TextEditingController ofertasController = TextEditingController();
  bool isLoading = false; // Para manejar la carga

  // Almacena el resultado
  String resultado = '';

  Process? _pythonProcess; // Variable para almacenar el proceso del servidor

  @override
  void initState() {
    super.initState();
    _startPythonServer();
  }

  Future<void> _startPythonServer() async {
    try {
      String pythonScriptPath =
          'C:/Users/santi/OneDrive/Documentos/Proyecto-ADA-II/Subasta_publica/app.py';
      _pythonProcess = await Process.start('python', [pythonScriptPath]);
      print('Servidor Python iniciado');

      // Escuchar la salida del proceso para depurar
      _pythonProcess!.stdout.transform(utf8.decoder).listen((data) {
        print(data);
      });
    } catch (e) {
      print('Error al iniciar el servidor: $e');
    }
  }

  @override
  void dispose() {
    if (kDebugMode) {
      print('dispose() llamado');
    } // Para verificar si se llama
    _stopPythonServer();
    super.dispose();
  }

  Future<void> _stopPythonServer() async {
    if (_pythonProcess != null) {
      // Intenta cerrar el proceso
      _pythonProcess!.kill();

      // Espera un poco para asegurarte de que el proceso se cierre
      await Future.delayed(
          const Duration(seconds: 1)); // Ajusta el tiempo si es necesario

      // Verifica si el proceso sigue corriendo
      print('Servidor cerrado.');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.grey[200],
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            _buildBarraFlotante(),
            const SizedBox(height: 16),
            Expanded(
              child: Row(
                children: [
                  _buildMenuIzquierdo(),
                  const SizedBox(width: 16),
                  _buildPanelContenido(), // Aquí se muestra la nueva UI
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }

  // Barra flotante estilo AppBar elevado
  Widget _buildBarraFlotante() {
    return Material(
      borderRadius: BorderRadius.circular(16), // Bordes redondeados
      child: Container(
        padding: const EdgeInsets.symmetric(vertical: 1.0, horizontal: 10.0),
        decoration: BoxDecoration(
          color: AppStyles.primaryColor,
          borderRadius: BorderRadius.circular(16),
        ),
        child: Row(
          children: [
            IconButton(
              icon: const Icon(Icons.arrow_back),
              color: AppStyles.buttonTextStyle.color,
              onPressed: () {
                Navigator.pop(context); // Volver a HomeScreen
              },
            ),
            const Spacer(),
            AnimatedSwitcher(
              duration: const Duration(milliseconds: 500),
              child: Text(titulo,
                  key: ValueKey(titulo),
                  style: AppStyles.buttonTextStyle
                      .copyWith(fontSize: 20, fontWeight: FontWeight.w300)),
            ),
            const Spacer(),
          ],
        ),
      ),
    );
  }

  // Menú Izquierdo
  Widget _buildMenuIzquierdo() {
    return Container(
      width: 200, // Ancho del menú
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(16),
      ),
      child: Column(
        children: [
          _buildTituloMenu(),
          const SizedBox(height: 10),
          _buildBotonesSolucion(),
          const Spacer(),
          _buildIconoDecorativo(),
        ],
      ),
    );
  }

  // Título del menú con animación
  Widget _buildTituloMenu() {
    return Container(
      width: 200, // Ancho del menú
      padding: const EdgeInsets.symmetric(vertical: 10.0, horizontal: 15.0),
      decoration: BoxDecoration(
        color: AppStyles.secondaryColor,
        borderRadius: BorderRadius.circular(16),
      ),
      child: Center(
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              'Subasta Pública',
              style: AppStyles.buttonTextStyle.copyWith(
                fontSize: 25,
              ),
            ),
            Text(
              subtitulo,
              style: AppStyles.infomationTextStyle
                  .copyWith(fontSize: 14, color: Colors.white),
            ),
            const SizedBox(height: 7),
          ],
        ),
      ),
    );
  }

  // Botones para los métodos de solución
  Widget _buildBotonesSolucion() {
    return Column(
      children: [
        _buildBotonSolucion('Dinámica', Icons.analytics, () {
          setState(() {
            titulo = 'Método Dinámico';
          });
        }),
        _buildBotonSolucion('Fuerza Bruta', Icons.memory, () {
          setState(() {
            titulo = 'Método Fuerza Bruta';
          });
        }),
        _buildBotonSolucion('Voraz', Icons.flash_on, () {
          setState(() {
            titulo = 'Método Voraz';
          });
        }),
      ],
    );
  }

  // Botón de solución con hover effect
  Widget _buildBotonSolucion(String texto, IconData icono, VoidCallback onTap) {
    return MouseRegion(
      onEnter: (_) => setState(() {
        hoveredButton = texto; // Indica que el mouse está sobre este botón
      }),
      onExit: (_) => setState(() {
        hoveredButton = ''; // Resetea cuando el mouse sale del botón
      }),
      child: InkWell(
        onTap: onTap,
        child: Padding(
          padding: const EdgeInsets.symmetric(vertical: 10.0, horizontal: 16.0),
          child: Row(
            children: [
              Icon(
                icono,
                color: hoveredButton == texto
                    ? Colors.amber
                    : AppStyles.primaryColor, // Cambia el color en hover
              ),
              const SizedBox(width: 8),
              Text(
                texto,
                style: TextStyle(
                  fontSize: 16,
                  color: hoveredButton == texto
                      ? AppStyles.primaryColor
                      : Colors.black, // Cambia el color del texto en hover
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  // Icono decorativo al final del menú
  Widget _buildIconoDecorativo() {
    return const Padding(
      padding: EdgeInsets.only(bottom: 16.0),
      child: Icon(Icons.android, size: 50, color: AppStyles.primaryColor),
    );
  }

  // Panel de contenido donde cambia la información según el botón seleccionado
  Widget _buildPanelContenido() {
    return Expanded(
      child: Material(
        borderRadius: BorderRadius.circular(16),
        child: Container(
          padding: const EdgeInsets.all(16.0),
          decoration: BoxDecoration(
            color: Colors.white,
            borderRadius: BorderRadius.circular(16),
          ),
          child: Column(
            children: [
              Text(
                'Método Dinámico',
                style: AppStyles.titleTextStyle.copyWith(fontSize: 20),
              ),
              const SizedBox(height: 16),
              _buildInputField(aController, 'Ingrese A'),
              _buildInputField(bController, 'Ingrese B'),
              _buildInputField(nController, 'Ingrese n'),
              _buildInputField(ofertasController,
                  'Ingrese ofertas (ej: [[precio1, minimo1, maximo1], ...])'),
              const SizedBox(height: 16),
              if (isLoading)
                const CircularProgressIndicator()
              else
                ElevatedButton(
                  onPressed: () {
                    if (aController.text.isNotEmpty &&
                        bController.text.isNotEmpty &&
                        nController.text.isNotEmpty &&
                        ofertasController.text.isNotEmpty) {
                      _runSubasta();
                    }
                  },
                  child: const Text('Ejecutar Algoritmo'),
                ),
              const SizedBox(height: 16),
              Text(resultado, style: const TextStyle(fontSize: 18)),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildInputField(TextEditingController controller, String label) {
    return TextField(
      controller: controller,
      decoration: InputDecoration(labelText: label),
      keyboardType: TextInputType.number,
    );
  }

  Future<void> _runSubasta() async {
    setState(() {
      isLoading = true;
      resultado = ''; // Reiniciar resultado
    });

    try {
      final response = await http.post(
        Uri.parse('http://127.0.0.1:5000/subasta'),
        headers: {'Content-Type': 'application/json'},
        body: json.encode({
          'A': int.parse(aController.text),
          'B': int.parse(bController.text),
          'n': int.parse(nController.text),
          'ofertas': json.decode(ofertasController
              .text), // Asegúrate de que la entrada esté en el formato correcto
        }),
      );

      if (response.statusCode == 200) {
        final data = json.decode(response.body);
        setState(() {
          resultado =
              'Valor final: ${data['valor_final']}\nMejor asignación: ${data['mejor_asignacion']}';
        });
      } else {
        setState(() {
          resultado = 'Error en la ejecución';
        });
      }
    } catch (e) {
      setState(() {
        resultado = 'Error: $e';
      });
    } finally {
      setState(() {
        isLoading = false; // Termina la carga
      });
    }
  }
}