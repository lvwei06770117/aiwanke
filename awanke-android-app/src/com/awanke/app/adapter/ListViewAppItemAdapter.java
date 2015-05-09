package com.awanke.app.adapter;

import java.util.List;

import com.awanke.app.R;
import com.awanke.app.bean.AppItem;
import com.awanke.app.common.BitmapManager;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

public class ListViewAppItemAdapter extends BaseAdapter {
	
	private Context 					context;
	private List<AppItem> 		listItems;
	private LayoutInflater 		listContainer;
	private int 						itemViewResource;
	private BitmapManager bmpManager;
	static class ListItemView{				
		public ImageView logo;
        public TextView appName;  
	    public TextView loveNum;
	    public TextView createDate;  
	    
	    public ImageView appImage;
	    public TextView appDesc;
	    public Button btnLove;
	    public Button btnRecommend;
	    public Button btnDownload;
	}

	public ListViewAppItemAdapter(Context context, List<AppItem> data,int resource) {
		this.context = context;			
		this.listContainer = LayoutInflater.from(context);	//鍒涘缓瑙嗗浘瀹瑰櫒骞惰缃笂涓嬫枃
		this.itemViewResource = resource;
		this.listItems = data;
	}

	@Override
	public int getCount() {
		return listItems.size();
	}

	@Override
	public Object getItem(int position) {
		return null;
	}

	@Override
	public long getItemId(int position) {
		return 0;
	}

	@Override
	public View getView(int position, View convertView, ViewGroup parent) {
			
		ListItemView  listItemView = null;
		if (convertView == null) {
			
			convertView = listContainer.inflate(this.itemViewResource, null);
			
			listItemView = new ListItemView();
			
			//listItemView.logo = (ImageView)convertView.findViewById(R.id.apps_listitem_logo);
			listItemView.appName = (TextView)convertView.findViewById(R.id.apps_listitem_name);
			//listItemView.loveNum= (TextView)convertView.findViewById(R.id.apps_listitem_loveNum);
			//listItemView.createDate= (TextView)convertView.findViewById(R.id.apps_listitem_date);
			
			//listItemView.appImage= (ImageView)convertView.findViewById(R.id.apps_listitem_cover);
			//listItemView.appDesc =  (TextView)convertView.findViewById(R.id.apps_listitem_desc);
			//listItemView.btnLove = (Button)convertView.findViewById(R.id.apps_listitem_btnLove);
			//listItemView.btnRecommend = (Button)convertView.findViewById(R.id.apps_listitem_btnRecommend);
			//listItemView.btnDownload = (Button)convertView.findViewById(R.id.apps_listitem_btnDownload);			
			
			//
			convertView.setTag(listItemView);
		}else {
			listItemView = (ListItemView)convertView.getTag();
		}	
		
		//
		AppItem appItem = listItems.get(position);
		listItemView.appName.setText(appItem.getAppName());		
		return convertView;		
	}

}
