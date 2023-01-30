package com.example.stt;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.speech.tts.TextToSpeech;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import java.util.Locale;

import static android.speech.tts.TextToSpeech.ERROR;

public class MainActivity extends AppCompatActivity {

    private TextToSpeech tts;              // TTS 변수 선언
    private EditText editText;
    private Button button01, button02, button03, button04, button05, button06;

    public MainActivity() {
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);


        editText = (EditText) findViewById(R.id.editText);
        button01 = (Button) findViewById(R.id.button01);
        button02 = (Button) findViewById(R.id.button02);
        button03 = (Button) findViewById(R.id.button03);
        button04 = (Button) findViewById(R.id.button04);
        button05 = (Button) findViewById(R.id.button05);
        button06 = (Button) findViewById(R.id.button06);

        Intent myIntent = new Intent(this, STTActivity.class);

        // TTS를 생성하고 OnInitListener로 초기화 한다.
        tts = new TextToSpeech(this, new TextToSpeech.OnInitListener() {
            @Override
            public void onInit(int status) {
                if(status != ERROR) {
                    // 언어를 선택한다.
                    tts.setLanguage(Locale.KOREAN);
                }
            }
        });
        button01.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                // editText에 있는 문장을 읽는다.
                tts.speak(editText.getText().toString(),TextToSpeech.QUEUE_FLUSH, null);
            }
        });
        button02.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                tts.setPitch(2.0f);         // 음성 톤을 2.0배 올려준다.
                tts.setSpeechRate(1.0f);    // 읽는 속도는 기본 설정
                // editText에 있는 문장을 읽는다.

                // speak() 메소드의 매개변수
                // 1. 음성 출력할 문장을 넘겨준다
                // 2. QUEUE_FLUSH : 진행중인 음성 출력을 끊고 이번 TTS의 음성 출력을 한다.
                // 3. null을 넘겨준다.
                tts.speak(editText.getText().toString(),TextToSpeech.QUEUE_FLUSH, null);
            }
        });
        button03.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                tts.setPitch(0.5f);         // 음성 톤을 0.5배 내려준다.
                tts.setSpeechRate(1.0f);    // 읽는 속도는 기본 설정

                // editText에 있는 문장을 읽는다.
                tts.speak(editText.getText().toString(),TextToSpeech.QUEUE_FLUSH, null);
            }
        });
        button04.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                tts.setPitch(1.0f);         // 음성 톤은 기본 설정
                tts.setSpeechRate(1.25f);    // 읽는 속도를 2배 빠르기로 설정
                // editText에 있는 문장을 읽는다.
                tts.speak(editText.getText().toString(),TextToSpeech.QUEUE_FLUSH, null);
            }
        });
        button05.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                tts.setPitch(1.0f);         // 음성 톤은 기본 설정
                tts.setSpeechRate(0.75f);    // 읽는 속도를 0.5빠르기로 설정
                // editText에 있는 문장을 읽는다.
                tts.speak(editText.getText().toString(),TextToSpeech.QUEUE_FLUSH, null);
            }
        });
        button06.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                startActivity(myIntent);
            }
        });

    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        // TTS 객체가 남아있다면 실행을 중지하고 메모리에서 제거한다.
        if(tts != null){
            tts.stop();
            tts.shutdown();
            tts = null;
        }
    }
}

