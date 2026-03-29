# PyInstaller yolunu kontrol et
PYINSTALLER := $(shell which pyinstaller)

install_deps:
	@if [ -z "$(PYINSTALLER)" ]; then \
		echo "PyInstaller bulunamadı. Kurulum deneniyor..."; \
		if command -v pipx > /dev/null; then \
			pipx install pyinstaller; \
		else \
			pip install pyinstaller; \
		fi \
	fi

# .py ile biten her şeyi yakala
%.py: install_deps
	@echo "--- DERLEME BAŞLIYOR: '$@' ---"
	# Tırnak işaretleri ($$@ yerine "$@") boşluklu isimler için hayat kurtarır
	@if command -v pyinstaller > /dev/null; then \
		pyinstaller --onefile --clean "$@"; \
	elif [ -f ~/.local/bin/pyinstaller ]; then \
		~/.local/bin/pyinstaller --onefile --clean "$@"; \
	else \
		echo "HATA: PyInstaller bulunamadı."; \
		exit 1; \
	fi
	@echo "------------------------------------------------"
	@echo "BAŞARILI! Dosyanız 'dist/' klasöründe."

clean:
	rm -rf build dist *.spec
