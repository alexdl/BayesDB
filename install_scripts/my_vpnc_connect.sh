#!/usr/bin/env bash


# test for root
if [[ "$USER" != "root" ]]; then
    echo "$0 must be executed as root"
    exit;
fi


# connect to VPN: must insert login credentials
vpnc-connect --gateway xdata.data-tactics-corp.com --id xdata && \
	route add -net 10.1.93.0 netmask 255.255.255.0 dev tun0 && \
	route add -net 10.1.92.0 netmask 255.255.255.0 dev tun0 && \
	route add -net 10.1.90.0 netmask 255.255.255.0 dev tun0 && \
	route del -net 0.0.0.0 tun0

# make sure /etc/resolv.conf works
> /etc/resolv.conf.tmp
for CONF_STR in "nameserver 10.1.90.10" \
	"nameserver 10.1.2.10" \
	"nameserver 127.0.0.1" \
	"search xdata.data-tactics-corp.com"
do
	if [[ -z $(grep "$CONF_STR" /etc/resolv.conf) ]]; then
		cat <(echo "$CONF_STR") >> /etc/resolv.conf.tmp
	fi
done
cat /etc/resolv.conf >> /etc/resolv.conf.tmp
cp /etc/resolv.conf.tmp /etc/resolv.conf
