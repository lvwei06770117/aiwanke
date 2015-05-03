package com.awanke.app.ui;

import java.util.ArrayList;
import java.util.List;

import com.awanke.app.R;
import com.awanke.app.adapter.ListViewAppItemAdapter;
import com.awanke.app.bean.AppItem;
import com.awanke.app.widget.PullToRefreshListView;

import android.app.Activity;
import android.os.Bundle;
import android.os.Handler;
import android.os.Message;

public class Main extends Activity {
	
	private PullToRefreshListView lvApps;
	private ListViewAppItemAdapter lvAppsAdapter;
	private List<AppItem> lvAppsData = new ArrayList<AppItem>();
	private Handler lvAppsHandler;
	
	private int lvAppsSumData;

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.main);
		
		//
		initAppsListView();
		//
		initAppListViewData();		
	}
	
	private void initAppsListView(){
		lvAppsAdapter = new ListViewAppItemAdapter(this,lvAppsData,R.layout.apps_listitem);
		lvApps = (PullToRefreshListView) findViewById(R.id.frame_listview_apps);
		lvApps.setAdapter(lvAppsAdapter);
		
	}
	
	private void initAppListViewData(){
		lvAppsHandler = new Handler(){
			public void handleMessage(Message msg) {
				if (msg.what >= 0) {
					// 
					List<AppItem> list = (ArrayList<AppItem>)msg.obj;
					lvAppsSumData = msg.what ;
					//
					int newdata = 0;					
					if (lvAppsData.size() > 0) {
						for (AppItem app1 : list) {
							boolean b = false;
							for(AppItem app2 :lvAppsData){
								if(app1.getId()==app2.getId()){
									b=true;
									break;
								}
							}
							if (!b)
								newdata++;
						}
					} else {
						newdata = lvAppsSumData;
					}
					
					lvAppsData.clear();				
					lvAppsData.addAll(list);
					lvAppsAdapter.notifyDataSetChanged();
					
				}
			}
		};		

		if(lvAppsData.isEmpty()){
			loadLvAppsData(0,lvAppsHandler);
		}
	}
	
	private void loadLvAppsData(final int pageIndex,final Handler handler){
		new Thread(){
			public void run(){
				Message msg = new Message();
				List<AppItem> list = new ArrayList<AppItem>();
				AppItem app = new AppItem();
				app.setAppName("game1");
				list.add(app);
				msg.what = 1;
				msg.obj = list;
				handler.sendMessage(msg);
			}
		}.start();
	}
	
}
