package com.awanke.app.common;

import java.io.File;
import java.io.IOException;
import java.lang.ref.SoftReference;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;
import java.util.WeakHashMap;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

import com.awanke.app.AppException;
import com.awanke.app.client.AppBaseClient;

import android.graphics.Bitmap;
import android.os.Handler;
import android.os.Message;
import android.widget.ImageView;

public class BitmapManager {
	
	private static HashMap<String, SoftReference<Bitmap>> cache;  
    private static ExecutorService pool;  
    private static Map<ImageView, String> imageViews;  
    private Bitmap defaultBmp;  
    
    static {  
        cache = new HashMap<String, SoftReference<Bitmap>>();  
        pool = Executors.newFixedThreadPool(5);  
        imageViews = Collections.synchronizedMap(new WeakHashMap<ImageView, String>());
    }  

public BitmapManager(){}
    
    public BitmapManager(Bitmap def) {
    	this.defaultBmp = def;
    }
    
    public void setDefaultBmp(Bitmap bmp) {  
    	defaultBmp = bmp;  
    }   
  
    public void loadBitmap(String url, ImageView imageView) {  
    	loadBitmap(url, imageView, this.defaultBmp, 0, 0);
    }
	
    public void loadBitmap(String url, ImageView imageView, Bitmap defaultBmp) {  
    	loadBitmap(url, imageView, defaultBmp, 0, 0);
    }
    
    public void loadBitmap(String url, ImageView imageView, Bitmap defaultBmp, int width, int height) {  
        imageViews.put(imageView, url);  
        Bitmap bitmap = getBitmapFromCache(url);  
   
        if (bitmap != null) {  
            imageView.setImageBitmap(bitmap);  
        } else {  
        	String filename = FileUtils.getFileName(url);
        	String filepath = imageView.getContext().getFilesDir() + File.separator + filename;
    		File file = new File(filepath);
    		if(file.exists()){		
    			Bitmap bmp = ImageUtils.getBitmap(imageView.getContext(), filename);
        		imageView.setImageBitmap(bmp);
        	}else{
        		imageView.setImageBitmap(defaultBmp);
        		queueJob(url, imageView, width, height);
        	}
        }  
    }  
  
    public Bitmap getBitmapFromCache(String url) {  
    	Bitmap bitmap = null;
        if (cache.containsKey(url)) {  
            bitmap = cache.get(url).get();  
        }  
        return bitmap;  
    }  
    
    public void queueJob(final String url, final ImageView imageView, final int width, final int height) {  
        /* Create handler in UI thread. */  
        final Handler handler = new Handler() {  
            public void handleMessage(Message msg) {  
                String tag = imageViews.get(imageView);  
                if (tag != null && tag.equals(url)) {  
                    if (msg.obj != null) {  
                        imageView.setImageBitmap((Bitmap) msg.obj);  
                        try {
							ImageUtils.saveImage(imageView.getContext(), FileUtils.getFileName(url), (Bitmap) msg.obj);
						} catch (IOException e) {
							e.printStackTrace();
						}
                    } 
                }  
            }  
        };  
  
        pool.execute(new Runnable() {   
            public void run() {  
                Message message = Message.obtain();  
                message.obj = downloadBitmap(url, width, height);  
                handler.sendMessage(message);  
            }  
        });  
    } 
  
    private Bitmap downloadBitmap(String url, int width, int height) {   
        Bitmap bitmap = null;
        try {
			bitmap = AppBaseClient.getNetBitmap(url);
			if(width > 0 && height > 0) {		
				bitmap = Bitmap.createScaledBitmap(bitmap, width, height, true);
			} 
			cache.put(url, new SoftReference<Bitmap>(bitmap));
		} catch (AppException e) {
			e.printStackTrace();
		}
        return bitmap;  
    }  
}
